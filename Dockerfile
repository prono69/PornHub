# We're using Ubuntu 20.10
FROM prono69/docker:groovy
 
#
# Clone repo and prepare working directory
#
RUN git clone https://github.com/prono69/PepeBot /root/userbot
RUN mkdir /root/userbot/bin
WORKDIR /root/userbot
#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/prono69/PepeBot/master/requirements.txt
CMD ["python3","-m","stdborg"]
