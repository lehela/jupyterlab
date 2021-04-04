#!/bin/bash

# Generate certificates
cd /usr/share/ca-certificates

openssl req \
	-x509 \
	-nodes \
	-days 365 \
	-newkey rsa:2048 \
	-keyout mykey.key \
	-out mycert.pem \
	-subj "/C=/ST=/L=/O=/OU=/CN="

mdkir /notebooks

jupyter notebook --generate-config
