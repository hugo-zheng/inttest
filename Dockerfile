FROM ubuntu:12.04

MAINTAINER hugozheng

RUN apt-get update
# ubuntu package
RUN apt-get install -y protobuf-compiler mono-gmcs
RUN apt-get install -y python python-dev python-distribute python-pip

# python package
RUN pip install gevent bottle pykka protobuf


ADD . /web_server
WORKDIR /web_server
EXPOSE 8088
CMD python ./listener.py

