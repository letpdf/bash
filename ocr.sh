#!/bin/bash

# USAGE
#./ocr.sh

# DEFAULT
NAME=$(basename "$0")
NAME=${NAME/.sh/}
#
LOGS="${NAME}.log.txt"
FOLDER_IN="${NAME}/in"
FOLDER_OUT="${NAME}/out"

## PREPARE
mkdir -p $FOLDER_IN
mkdir -p $FOLDER_OUT
echo "INPUT:"

# START
LIST=$(ls "$FOLDER_IN/")
for FILENAME in $LIST; do

  FILE_PATH="${FOLDER_IN}/${FILENAME}"
  echo $FILE_PATH

  [ ! -f ${FILE_PATH} ] && echo "!!! FILE/FOLDER ${FILE_PATH} NOT EXIST" >>$LOGS && exit
  FOLDER_OUT_FILE="${FOLDER_OUT}/${FILENAME}"
  echo -n "" > $FOLDER_OUT_FILE

  while
    LINE=
    IFS=$' \t\r\n' read -r LINE || [[ $LINE ]]
  do
    [ -z "$LINE" ] && echo "REMOVED: $LINE" >>$LOGS && continue

    echo "$LINE"
    #echo "$LINE" >> $FOLDER_OUT_FILE
    #./ocr_folder.sh "$LINE" >> $FOLDER_OUT_FILE

  done <"$FILE_PATH"

done

echo ""
echo "OUTPUT:"
cat $FOLDER_OUT_FILE
