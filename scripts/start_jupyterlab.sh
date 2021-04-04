#!/bin/bash

jupyter lab \
    --certfile=/usr/share/ca-certificates/jupyterlab_cert.pem \
    --keyfile=/usr/share/ca-certificates/jupyterlab_key.key \
    --notebook-dir=/home/jupyterlab/notebooks \
    --no-browser \
    --ip=0.0.0.0 \
    --allow-root