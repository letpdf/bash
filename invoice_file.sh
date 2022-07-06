#!/bin/bash

# USAGE
#./invoice.sh INPUT_FOLDER CHECK_IN_FOLDER_YEAR COMPANY
#./invoice.sh ionos_2020 2020 ionos
#./invoice.sh ionos_2021 2021 ionos
#./invoice.sh strato2020/done 2020 strato
#./invoice.sh strato2021 2021 strato
#./invoice.sh all-2020/01 2020

# DEFAULT
NAME=$(basename "$0")
NAME=${NAME/.sh/}
#
FTIME="$(date +%s)"
LOGS_FOLDER="${NAME}/.logs"
mkdir -p $LOGS_FOLDER
LOGS="${LOGS_FOLDER}/${FTIME}.txt"
#[ ! -f "${LOGS}" ] &&
echo -n "" > $LOGS

## PARAMS
FOLDER=$1
[ -z "$FOLDER" ] && echo "!!! FOLDER empty" >>$LOGS && cat $LOGS && exit

FOLDER_YEAR=$2
[ -z "$FOLDER_YEAR" ] && echo "!!! YEAR FOLDER empty" >>$LOGS && cat $LOGS && exit

COMPANY=$3
#[ -z "$COMPANY" ] && echo "!!! COMPANY FOLDER empty" >>$LOGS && cat $LOGS && exit

# FOLDER DATA
FOLDER_IN="${NAME}/in"
FOLDER_OUT="${NAME}/out"
FOLDER_DUPLICATED="${NAME}/duplicated"
FOLDER_UNDEFINED="${NAME}/undefined"

## PREPARE
mkdir -p $FOLDER_IN
mkdir -p $FOLDER_OUT
mkdir -p $FOLDER_DUPLICATED
mkdir -p $FOLDER_UNDEFINED
echo "INPUT:"

# START
CHECK="$FOLDER_IN/$FOLDER"
## FIND only ended on pdf
LIST=$(ls ${CHECK} | grep -E 'pdf$')
for FILENAME in $LIST; do
  echo "$FILENAME"
  #exit
  FILE_PATH="${CHECK}/${FILENAME}"
  [ ! -f ${FILE_PATH} ] && continue

  echo "$FILE_PATH" >>$LOGS
  echo "PATH: [$FOLDER] FILE: [$FILENAME] TO [$FOLDER_YEAR] COMPANY [$COMPANY]"

  #CHECK_FOLDER="${FOLDER_YEAR}/${FILENAME}"

  # check if file exist in year
  #RESULT=$(find $FOLDER_YEAR -name "$FILENAME" -type f)
  if [ $(find $FOLDER_YEAR -name "$FILENAME" -type f | wc -l) -gt 0 ]; then
    #cp $FILE_PATH $FOLDER_YEAR && echo "COPIED: [$FILE_PATH] TO [$FOLDER_YEAR]" >>$LOGS
    echo "FOUND: [$FILENAME]  IN [$FOLDER_YEAR]" >>$LOGS
    TARGET=$FOLDER_DUPLICATED
    JPG_FILE="${FILE_PATH}0.jpg"
    TXT_FILE="${JPG_FILE}.txt"
    DATE_FILE="${JPG_FILE}.date"
  #if exist or move to duplicated
    echo "DUPLICATED: [$FILE_PATH] TO [$TARGET]" >>$LOGS
  else
    echo "NOT FOUND: [$FILENAME]  IN [$FOLDER_YEAR]" >>$LOGS
    #Check OCR
    ## prepare image and extract string
    #RESULT=$(python3 pdf2jpg.py $FILE_PATH)
    python3 pdf2jpg.py $FILE_PATH
    #python3 jpg2txt.py invoice/in/ionos_2020/RG_100080295635.pdf0.jpg
    #./extract.sh in/ionos_2020/RG_100080295635.pdf0.jpg.txt
    #./extract.php.sh in/ionos_2020/RG_100080295635.pdf0.jpg.txt
    #php extract.php in/ionos_2020/RG_100080295635.pdf0.jpg.txt

    JPG_FILE="${FILE_PATH}0.jpg"
    #echo $JPG_FILE
    python3 jpg2txt.py $JPG_FILE
    #RESULT=$(python3 jpg2txt.py $FILE_PATH)
    #sleep 1
    TXT_FILE="${JPG_FILE}.txt"
    #DATE_FILE="${FILE_PATH}0.jpg.my"
    DATE_VAL=$(php invoice_date.php $TXT_FILE)
    DATE_FILE="${JPG_FILE}.date"
    echo -n "$DATE_VAL" > $DATE_FILE

    #cat "${TXT_FILE}"

    #Find Month
    FOLDER_MONTH=$(php invoice_my.php $TXT_FILE)
    echo "$FOLDER_MONTH"

    if [ -z "$FOLDER_MONTH" ] || [ "${#FOLDER_MONTH}" -gt "10" ]; then
      # undefined data
      TARGET=$FOLDER_UNDEFINED
      echo "UNDEFINED: [$FOLDER_MONTH] TO [$TARGET]" >>$LOGS
    else
      # correct data format
      TARGET="$FOLDER_YEAR/$FOLDER_MONTH/$COMPANY"
      echo "DETECTED: [$FOLDER_MONTH] TO [$TARGET]" >>$LOGS
    fi
    #exit
  fi

  mkdir -p $TARGET

  # Move to the Target
  mv $FILE_PATH $TARGET && echo "MOVED: [$FILE_PATH] TO [$TARGET]" >>$LOGS
  [ -f "$JPG_FILE" ] && mv $JPG_FILE $TARGET && echo "MOVED: [$JPG_FILE] TO [$TARGET]" >>$LOGS
  [ -f "$DATE_FILE" ] && mv $DATE_FILE $TARGET && echo "MOVED: [$DATE_FILE] TO [$TARGET]" >>$LOGS
  [ -f "$TXT_FILE" ] && mv $TXT_FILE $TARGET && echo "MOVED: [$TXT_FILE] TO [$TARGET]" >>$LOGS

done

echo ""
echo "OUTPUT:"
cat $LOGS
