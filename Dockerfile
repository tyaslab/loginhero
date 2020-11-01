FROM ubuntu:18.04 AS base
RUN apt update -y
RUN apt install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa -y
RUN apt update -y
RUN apt install python3.8 python3.8-dev python3.8-venv python3-pip build-essential -y
RUN python3.8 -m venv env