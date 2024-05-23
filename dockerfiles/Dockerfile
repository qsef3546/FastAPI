FROM ubuntu:22.04

#OS 업데이트
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install python3.11 -y
RUN apt-get install iputils-ping -y
RUN apt-get install python3-pip -y

RUN apt-get install -y curl
RUN apt-get install -y wget
RUN apt-get install -y openssh-server
RUN apt-get install -y net-tools
RUN apt-get install -y vim
RUN apt-get install -y cron
COPY requirements.txt ./
ARG DEBIAN_FRONTEND=noninteractive
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt
WORKDIR /workspace

#지역 설정/ 시간

ENV TZ=Asia/Seoul
RUN apt-get install -y tzdata
#locale 설정
ENV LC_ALL=C.UTF-8
ENV LANGUAGE=ko