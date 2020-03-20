#!/bin/sh
# @AUTHOR: imyme6yo "imyme6yo@gmail.com"
# @DRAFT: 20200320
# remove docker image
docker ps -a | grep pycrypt:dev | awk '{print $1}'| xargs docker stop
# stop & rm docker container
docker ps -a | grep pycrypt:dev | awk '{print $1}'| xargs docker rm
docker images | grep pycrypt:dev | awk '{print $3}'| xargs docker rmi
# build image
docker build -t pycrypt:dev .
# run container
docker run --rm -it -v $(pwd):/code  pycrypt:dev sh /${DIR}/startup.sh