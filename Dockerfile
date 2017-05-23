FROM centos:7

MAINTAINER Swapnil Kulkarni <me@coolsvap.net>

RUN yum -y update && yum clean all
	
RUN yum -y install \
    epel-release \
  && yum clean all
RUN yum -y install \
    python-devel \
    python-pip \
  && yum clean all
  
COPY src/ /app/referee
WORKDIR /app/referee
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["server.py"]
