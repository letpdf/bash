#!/bin/bash

# USAGE
#./ocr_folder.sh 2020/*/strato
#./ocr_folder.sh 2021/*/strato

# DEFAULT
NAME=$(basename "$0")
NAME=${NAME/.sh/}
LOGS="${NAME}.log.txt"
#
FOLDER_IN="${NAME}/in"
FOLDER_OUT="${NAME}/out"

# PARAMS
#(($# != 4)) && echo "!!! RECEIVER SUBJECT MESSAGE ATTACHMENT" >>$LOGS && exit
(($# != 1)) && echo "!!! MUST BE ONE PARAM: FOLDER OR Add a QUOOTAS between params" >>$LOGS && cat $LOGS && exit

FOLDER=$1
[ -z "$FOLDER" ] && echo "!!! FOLDER empty" >>$LOGS && cat $LOGS && exit

#set -x

FOLDER_LIST=$(ls -d ${FOLDER})
#echo $FOLDER_LIST
for FOLDER in $FOLDER_LIST; do
  #echo $FOLDER
  LIST=$(ls "$FOLDER")
  for FILENAME in $LIST; do

    #echo $FILENAME
    FILE_IN="${FOLDER}${FILENAME}/"
    echo $FILE_IN

    #FILE_OUT="${FOLDER}/${FILENAME}.txt"
    #echo $FILE_OUT

    python3 pdf2txt.py "$FILE_IN"
    #python3 pdf2txt.py "$FILENAME"
    #exit
    #continue
    #python3 pdf2txt.py "/media/tom/projects/softreck-invoices/2020/06.2020/"

    #./email_curl.sh "$RECEIVER" "$SUBJECT" "$MESSAGE" "$ATTACHMENT" >> $OUT_FILE
  done
done
