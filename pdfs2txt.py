import cv2
import pytesseract
import numpy as np
from sys import argv
from invoice2data import extract_data
from invoice2data.extract.loader import read_templates
import yaml
import glob
import errno
import os
import pymongo
#jpg_path="pdf/RG_100068630897.pdf0.jpg"
# Import Python json module
import json

if len(argv) > 1:
    jpg_path = argv[1]
else:
    jpg_path = input('pdf file path>>> ')

try:
    # Store Pdf with convert_from_path function
    print(jpg_path)
    read_template = read_templates(folder="invoice_templates")
    pdfFiles = []
    pdfFiles1 = []
    pdfFiles2 = []
    filenames=[]
    path_filename=[]

    for filename in os.listdir(jpg_path):
        if filename.endswith(".pdf"):
            filenames.append(filename)
            pathname = jpg_path+str(filename)
            print(pathname)
            #path_filename.append(pathname)
            result = extract_data(pathname, read_template)
            print(result)
            #exit()

            result['date']=result['date'].strftime("%d.%m.%Y")

            if "sale_date" in result:
                result['sale_date']=result['sale_date'].strftime("%d.%m.%Y")

            if "subscription_date" in result:
                result['subscription_date']=result['subscription_date'].strftime("%d.%m.%Y")

            print(result)
            print("----------------------")
            if (result==False):
                #pdfFiles.append(filename)
                exit()
            else:
                #pdfFiles.append(result)
                with open(pathname + ".json", 'w') as file:
                    file.write(json.dumps(result))

                with open(pathname + ".date", 'w') as file:
                    file.write(str(result['date']))

                with open(pathname + ".price", 'w') as file:
                    file.write(str(result['amount']))

                with open(pathname + ".number", 'w') as file:
                    file.write(str(result['invoice_number']))

                with open(pathname + ".currency", 'w') as file:
                    currency=str(result['currency'])
                    currency=currency.replace("€", "EUR" )
                    currency=currency.replace("$", "USD" )
                    file.write(currency)

    #image = cv2.imread(jpg_path)
    #custom_config = r'--oem 3 --psm 6'
    #txt_content = (pytesseract.image_to_string(image, config=custom_config))
    #with open(jpg_path + ".txt", 'w') as file:
    #    file.write(txt_content)


except FileNotFoundError:
    print(f'{argv[1]} not found')

except TypeError as error:
    print(error)

