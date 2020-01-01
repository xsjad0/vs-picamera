#!/usr/bin/env bash

docker run -ti --restart=always --device /dev/vchiq -p 1883:1883 vs-rembold-mqtt