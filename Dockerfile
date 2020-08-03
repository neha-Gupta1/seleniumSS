FROM ubuntu:18.04

RUN apt-get update && apt-get install -y \
    software-properties-common

RUN add-apt-repository universe
RUN apt update
RUN apt install -y python3.8
RUN apt-get install -y wget
RUN apt install -y python3-pip

#download and install chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt install -y ./google-chrome-stable_current_amd64.deb

#download and install firefox
RUN apt install -y firefox

RUN export LC_ALL=en_US.utf-8 && export LANG=en_US.utf-8
#install python dependencies
COPY requirements.txt requirements.txt 
RUN pip3 install -r ./requirements.txt 

#some envs
ENV APP_HOME /app 

#set workspace
WORKDIR ${APP_HOME}

#copy local files
COPY . . 

EXPOSE 5000

 CMD python3 app.py
#ENTRYPOINT [ "python" ]
#CMD [ "app.py" ]
