#!/usr/bin/env bash

docker run -d --restart=always --device /dev/vchiq -p 8080:8080 vs-rembold-web