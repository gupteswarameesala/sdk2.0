#!/bin/bash
project=helloworld-endpoint

echo "---------------------------------------------"
echo "Building ${project} docker image...!!"
docker build -t ${project}:2.0.1 .
echo "---------------------------------------------"

