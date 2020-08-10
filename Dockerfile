#  creates a layer from the base Docker image.
FROM python:3.8.5-slim-buster
 
WORKDIR /app
# https://shouldiblamecaching.com/
ENV PIP_NO_CACHE_DIR 1
 
# fix "ephimeral" / "AWS" file-systems
RUN sed -i.bak 's/us-west-2\.ec2\.//' /etc/apt/sources.list
# to resynchronize the package index files from their sources.
RUN apt -qq update
# base required pre-requisites before proceeding ...
RUN apt -qq install -y --no-install-recommends curl git gnupg2 wget
# add required files to sources.list
RUN wget -q -O - https://mkvtoolnix.download/gpg-pub-moritzbunkus.txt | apt-key add - && \
    wget -qO - https://ftp-master.debian.org/keys/archive-key-10.asc | apt-key add -
RUN sh -c 'echo "deb https://mkvtoolnix.download/debian/ buster main" >> /etc/apt/sources.list.d/bunkus.org.list' && \
    sh -c 'echo deb http://deb.debian.org/debian buster main contrib non-free | tee -a /etc/apt/sources.list'
# to resynchronize the package index files from their sources.
RUN apt -qq update
# http://bugs.python.org/issue19846
# https://github.com/SpEcHiDe/PublicLeech/pull/97
ENV LANG C.UTF-8
 
# we don't have an interactive xTerm
ENV DEBIAN_FRONTEND noninteractive
 
# install google chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    dpkg -i ./google-chrome-stable_current_amd64.deb && \
    rm ./google-chrome-stable_current_amd64.deb
# install chromedriver
RUN mkdir /tmp/ && \
    wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE)/chromedriver_linux64.zip  && \
    unzip /tmp/chromedriver.zip chromedriver -d /usr/bin/ && \
    rm /tmp/chromedriver.zip
# install required packages
RUN apt -qq install -y --no-install-recommends \
    # we need Python, since it is a Python application
    python3 python3-pip \
    # this package is required to fetch "contents" via "TLS"
    apt-transport-https \
    # install coreutils
    coreutils aria2 jq pv \
    # install encoding tools
    ffmpeg mediainfo rclone \
    # install extraction tools
    mkvtoolnix \
    p7zip rar unrar zip unzip \
    # miscellaneous helpers
    megatools mediainfo rclone && \
    rm -rf /var/lib/apt/lists /var/cache/apt/archives /tmp
 
# each instruction creates one layer
# Only the instructions RUN, COPY, ADD create layers.
# copies 'requirements', to inside the container
COPY . .
# install requirements, inside the container
RUN pip3 install --no-cache-dir -r requirements.txt
# adds files from your Docker client’s current directory.
# COPY . .
 
# specifies what command to run within the container.
CMD ["python3", "-m", "stdborg"]
