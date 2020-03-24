#!/bin/sh
# @AUTHOR: imyme6yo "imyme6yo@gmail.com"
# @DRAFT: 20200320
# @UPDATE: 20200324
# stop docker container
docker ps -a | grep mycrypto:dev | awk '{print $1}'| xargs docker stop
# remove docker container
docker ps -a | grep mycrypto:dev | awk '{print $1}'| xargs docker rm
# remove docker image
docker images | grep mycrypto:dev | awk '{print $3}'| xargs docker rmi
# build image
docker build -t mycrypto:dev .
# run container
docker run --rm -it -v $(pwd):/code  mycrypto:dev sh /code/project.sh