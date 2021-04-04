#!/bin/bash

NB_UID=$1
NB_GID=$2

# Generate certificates
openssl req \
	-x509 \
	-nodes \
	-days 365 \
	-newkey rsa:2048 \
	-keyout /usr/share/ca-certificates/jupyterlab_key.key \
	-out /usr/share/ca-certificates/jupyterlab_cert.pem \
	-subj "/C=/ST=/L=/O=/OU=/CN="

chmod 644 /usr/share/ca-certificates/jupyterlab*

# Add non-root user to run jupyterlabs
addgroup \
	--gid $NB_GID \
	jupyterlab

adduser \
	--uid $NB_UID \
	--gid $NB_GID \
	--disabled-password \
	--gecos "" \
	jupyterlab
