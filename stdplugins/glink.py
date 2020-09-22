"""Upload link to gDrive
Syntax:
.glink"""
import asyncio
import math
import os
import time
from datetime import datetime
from mimetypes import guess_type

import httplib2
from apiclient.http import MediaFileUpload
from googleapiclient.discovery import build
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.file import Storage
from pySmartDL import SmartDL
from telethon import events

from uniborg.util import admin_cmd, humanbytes, progress

# Path to token json file, it should be in same directory as script
G_DRIVE_TOKEN_FILE = Config.TMP_DOWNLOAD_DIRECTORY + "/auth_token.txt"
# Copy your credentials from the APIs Console
CLIENT_ID = Config.G_DRIVE_CLIENT_ID
CLIENT_SECRET = Config.G_DRIVE_CLIENT_SECRET
# Check https://developers.google.com/drive/scopes for all available scopes
OAUTH_SCOPE = "https://www.googleapis.com/auth/drive.file"
# Redirect URI for installed apps, can be left as is
REDIRECT_URI = "urn:ietf:wg:oauth:2.0:oob"
# global variable to set Folder ID to upload to
parent_id = Config.GDRIVE_FOLDER_ID


@borg.on(admin_cmd(pattern="glink ?(.*)", allow_sudo=True))
async def download(dryb):
    """ For .gdrive command, upload files to google drive. """
    if not dryb.text[0].isalpha() and dryb.text[0] not in ("/", "#", "@", "!"):
        if dryb.fwd_from:
            return
        await dryb.edit("Processing ...")
        input_str = dryb.pattern_match.group(1)
        if CLIENT_ID is None or CLIENT_SECRET is None:
            return false
        if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
            os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
            required_file_name = None
        elif input_str:
            start = datetime.now()
            url = input_str
            file_name = os.path.basename(url)
            if "|" in input_str:
                url, file_name = input_str.split("|")
            url = url.strip()
            file_name = file_name.strip()
            downloaded_file_name = Config.TMP_DOWNLOAD_DIRECTORY + "" + file_name
            downloader = SmartDL(url, downloaded_file_name, progress_bar=False)
            downloader.start(blocking=False)
            c_time = time.time()
            display_message = None
            while not downloader.isFinished():
                status = downloader.get_status().capitalize()
                total_length = downloader.filesize if downloader.filesize else None
                downloaded = downloader.get_dl_size()
                now = time.time()
                diff = now - c_time
                percentage = downloader.get_progress() * 100
                downloader.get_speed()
                round(diff) * 1000
                progress_str = "[{0}{1}]\nProgress: {2}%".format(
                    "".join(["●" for i in range(math.floor(percentage / 5))]),
                    "".join(["○" for i in range(20 - math.floor(percentage / 5))]),
                    round(percentage, 2),
                )
                estimated_total_time = downloader.get_eta(human=True)
                try:
                    current_message = f"{status}...\nURL: {url}\nFile Name: {file_name}\n{progress_str}\n{humanbytes(downloaded)} of {humanbytes(total_length)}\nETA: {estimated_total_time}"
                    if current_message != display_message:
                        await dryb.edit(current_message)
                        display_message = current_message
                        await asyncio.sleep(3)
                except Exception as e:
                    logger.info(str(e))
            end = datetime.now()
            ms = (end - start).seconds
            if downloader.isSuccessful():
                await dryb.edit(
                    "Downloaded to `{}` in {} seconds.\nNow Uploading to Google Drive...".format(
                        downloaded_file_name, ms
                    )
                )
                required_file_name = downloaded_file_name
            else:
                await dryb.edit("Incorrect URL\n{}".format(url))
        elif dryb.reply_to_msg_id:
            start = datetime.now()
            try:
                c_time = time.time()
                downloaded_file_name = await dryb.client.download_media(
                    await dryb.get_reply_message(),
                    Config.TMP_DOWNLOAD_DIRECTORY,
                    progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                        progress(d, t, dryb, c_time, "Downloading...")
                    ),
                )
            except Exception as e:  # pylint:disable=C0103,W0703
                await dryb.edit(str(e))
            else:
                end = datetime.now()
                required_file_name = downloaded_file_name
                ms = (end - start).seconds
                await dryb.edit(
                    "Downloaded to `{}` in {} seconds.\nNow Uploading to GDrive...".format(
                        required_file_name, ms
                    )
                )

    if required_file_name:
        #
        if Config.G_DRIVE_AUTH_TOKEN_DATA is not None:
            with open(G_DRIVE_TOKEN_FILE, "w") as t_file:
                t_file.write(Config.G_DRIVE_AUTH_TOKEN_DATA)
        # Check if token file exists, if not create it by requesting
        # authorization code
        if not os.path.isfile(G_DRIVE_TOKEN_FILE):
            storage = await create_token_file(G_DRIVE_TOKEN_FILE, dryb)
            http = authorize(G_DRIVE_TOKEN_FILE, storage)
        # Authorize, get file parameters, upload file and print out result URL
        # for download
        http = authorize(G_DRIVE_TOKEN_FILE, None)
        file_name, mime_type = file_ops(required_file_name)
        # required_file_name will have the full path
        # Sometimes API fails to retrieve starting URI, we wrap it.
        try:
            g_drive_link = await upload_file(
                http, required_file_name, file_name, mime_type, dryb
            )
            await dryb.edit(
                f"File:`{required_file_name}`\nHas Successfully Uploaded to : [Google Drive]({g_drive_link})"
            )
        except Exception as e:
            await dryb.edit(
                f"Error while uploading to Google Drive\nError Code:\n`{e}`"
            )


# Get mime type and name of given file
def file_ops(file_path):
    mime_type = guess_type(file_path)[0]
    mime_type = mime_type if mime_type else "text/plain"
    file_name = file_path.split("/")[-1]
    return file_name, mime_type


async def create_token_file(token_file, event):
    # Run through the OAuth flow and retrieve credentials
    flow = OAuth2WebServerFlow(
        CLIENT_ID, CLIENT_SECRET, OAUTH_SCOPE, redirect_uri=REDIRECT_URI
    )
    authorize_url = flow.step1_get_authorize_url()
    async with event.client.conversation(Config.PRIVATE_GROUP_BOT_API_ID) as conv:
        await conv.send_message(
            f"Go to the following link in your browser: {authorize_url} and reply the code"
        )
        response = conv.wait_event(
            events.NewMessage(outgoing=True, chats=Config.PRIVATE_GROUP_BOT_API_ID)
        )
        response = await response
        code = response.message.message.strip()
        credentials = flow.step2_exchange(code)
        storage = Storage(token_file)
        storage.put(credentials)
        return storage


def authorize(token_file, storage):
    # Get credentials
    if storage is None:
        storage = Storage(token_file)
    credentials = storage.get()
    # Create an httplib2.Http object and authorize it with our credentials
    http = httplib2.Http()
    credentials.refresh(http)
    http = credentials.authorize(http)
    return http


async def upload_file(http, file_path, file_name, mime_type, event):
    # Create Google Drive service instance
    drive_service = build("drive", "v2", http=http, cache_discovery=False)
    # File body description
    media_body = MediaFileUpload(file_path, mimetype=mime_type, resumable=True)
    body = {
        "title": file_name,
        "description": "Uploaded using PaperplaneExtended Userbot.",
        "mimeType": mime_type,
    }
    if parent_id:
        body["parents"] = [{"id": parent_id}]
    # Permissions body description: anyone who has link can upload
    # Other permissions can be found at
    # https://developers.google.com/drive/v2/reference/permissions
    permissions = {"role": "reader", "type": "anyone", "value": None, "withLink": True}
    # Insert a file
    file = drive_service.files().insert(body=body, media_body=media_body)
    response = None
    while response is None:
        status, response = file.next_chunk()
        await asyncio.sleep(20)
        if status:
            percentage = int(status.progress() * 100)
            progress_str = "[{0}{1}]\nProgress: {2}%\n".format(
                "".join(["●" for i in range(math.floor(percentage / 5))]),
                "".join(["○" for i in range(20 - math.floor(percentage / 5))]),
                round(percentage, 2),
            )
            await event.edit(
                f"Uploading to Google Drive...\n\nFile Name: {file_name}\n{progress_str}"
            )
    if file:
        await event.edit(file_name + " Uploaded Successfully")
    # Insert new permissions
    drive_service.permissions().insert(
        fileId=response.get("id"), body=permissions
    ).execute()
    # Define file instance and get url for download
    file = drive_service.files().get(fileId=response.get("id")).execute()
    return response.get("webContentLink")


@borg.on(admin_cmd(pattern="gfolder ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    folder_link = "https://drive.google.com/drive/u/2/folders/" + parent_id
    await event.edit(
        f"Your current Google Drive Upload Directory : [Here]({folder_link})"
    )
