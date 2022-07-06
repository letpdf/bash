#!/bin/bash

# USAGE
#./pdf2txt.sh /media/tom/projects/softreck-invoices/2020/12.2020/ionos/RG_100081390203.pdf

# START
FILE_PATH=$1
[ -z "$FILE_PATH" ] && echo "!!! FILE_PATH IS EMPTY" && exit
[ ! -f ${FILE_PATH} ] && echo "!!! FILE ${FILE_PATH} NOT EXIST" && exit
python3 pdf2txt.py $FILE_PATH