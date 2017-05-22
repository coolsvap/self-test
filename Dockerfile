FROM coolsvap/centos-python:latest

COPY build.sh /build/build.sh

RUN chmod +x /build/build.sh
