FROM coolsvap/centos-python:latest

COPY build.sh /tmp/build.sh

RUN ['chmod', '+x', '/tmp/build.sh']
RUN ['./tmp/build.sh']
