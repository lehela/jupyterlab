#!/bin/bash

jupyter lab \
    --certfile=/usr/share/ca-certificates/mycert.pem \
    --keyfile=/usr/share/ca-certificates/mykey.key \
    --notebook-dir=/notebooks \
    --no-browser \
    --ip=0.0.0.0 \
    --allow-root