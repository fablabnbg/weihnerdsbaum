#! /bin/sh
file=$1 
test -z "$file" && file=main.py
set -x
curl -# --user micro:python -T $file ftp://192.168.1.1/flash/$file --user micro:python
