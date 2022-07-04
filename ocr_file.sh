#!/bin/bash

# USAGE
#./ocr.sh

# DEFAULT
NAME=$(basename "$0")
NAME=${NAME/.sh/}
LOGS="${NAME}.log.txt"
FOLDER_IN="${NAME}/in"
FOLDER_OUT="${NAME}/out"

## PREPARE
mkdir -p $FOLDER_IN
mkdir -p $FOLDER_OUT
echo "INPUT:"

(($# != 1)) && echo "!!! MUST BE ONE PARAM: PATH OR Add a QUOOTAS between params" >>$LOGS && cat $LOGS && exit

FILE_PATH=$1
[ -z "$FILE_PATH" ] && echo "!!! FILE_PATH empty" >>$LOGS && cat $LOGS && exit
[ ! -f ${FILE_PATH} ] && echo "!!! FILE_PATH ${FILE_PATH} NOT EXIST" >>$LOGS && cat $LOGS && exit

echo ""
echo "OUTPUT:"
cat $FOLDER_OUT_FILE
