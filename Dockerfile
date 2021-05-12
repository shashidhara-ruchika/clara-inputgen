# Docker build script for clara ipgen

FROM ubuntu:18.04
FROM python:3.7


# Update and install required software
RUN apt-get -y update
RUN apt-get -y install python-pip gcc make cython lp-solve liblpsolve55-dev git
RUN apt-get -y install nano

RUN apt-get -y install python3
RUN apt-get -y install python3-pip 

RUN apt-get -y install ocaml
RUN apt-get -y install ocamlbuild
RUN apt-get -y install ocaml-findlib

RUN apt-get -y install mime-support

RUN pip3 install cython

RUN pip3 install pycparser
RUN pip3 install astor
RUN pip3 install anytree
RUN pip3 install covgen


# Install ipgen
WORKDIR /root/
RUN mkdir ipgen
#RUN mkdir ipgen/
ADD ipgen/ ipgen/

WORKDIR /root/ipgen/clara
RUN make install

WORKDIR /root/ipgen/crest/cil
RUN ./configure
RUN make -pie

WORKDIR /root/ipgen/crest/src
RUN make -pie

WORKDIR /root/ipgen/crest/interface
RUN chmod 777 interface.sh

ARG buildtime_variable=/usr/lib/lp_solve
ENV LD_LIBRARY_PATH=$buildtime_variable

WORKDIR /root/ipgen
RUN chmod 777 test1.sh
RUN chmod 777 test2.sh

WORKDIR /root/ipgen/crest/interface
