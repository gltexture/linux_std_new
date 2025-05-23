#!/bin/bash

podman run -d --net=host -p 8086:8086 --name app01 app1
