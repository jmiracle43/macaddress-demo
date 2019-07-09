#!/bin/sh
docker run -e MAC_API_KEY -it macaddress-io-tools:latest "$@"
