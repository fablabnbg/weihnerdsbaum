#! /bin/sh
file=$1 
test -z "$file" && file=out.txt
set -x
curl --user micro:python ftp://192.168.1.1/flash/$file
