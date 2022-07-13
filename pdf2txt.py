from sys import argv
from invoice2data import extract_data
from invoice2data.extract.loader import read_templates
import json
import os
import zoneinfo
from datetime import datetime
import pytz
import warnings
import dateparser

# Ignore dateparser warnings regarding pytz
warnings.filterwarnings(
    "ignore",
    message="The localize method is no longer necessary, as this time zone supports the fold attribute",
)

NYC = zoneinfo.ZoneInfo("America/New_York")
datetime(2020, 1, 1, tzinfo=NYC)

ALLOWED_EXTENSIONS = set(['pdf'])
DATE_FORMAT = "%d.%m.%Y"


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def currency_data_to_float(ammount):
    return float(ammount.replace(',', '').replace('$', ''))


def getDate(input):
    #print(input)
    if type(input) is list:
        if input:
            return input[0].strftime(DATE_FORMAT)
    return input.strftime(DATE_FORMAT)


def exchangeDate(array, key):
    #print(type(array))
    #print(array)
    #print(key)
    if key in array:
        #print(type(array[key]))
        if array[key]:
            if type(array[key]) is list:
                array[key] = array[key][0].strftime(DATE_FORMAT)
            elif type(array[key]) is dict:
                array[key] = array[key][0].strftime(DATE_FORMAT)
            else:
                array[key] = array[key].strftime(DATE_FORMAT)
    return array


def exchangeInvoiceNumber(array, key):
    #print(type(array))
    #print(array)
    #print(key)
    if key in array:
        #print(type(array[key]))
        if array[key]:
            if type(array[key]) is list:
                array[key] = str(array[key][0])
            elif type(array[key]) is dict:
                array[key] = str(array[key][0])
            else:
                array[key] = str(array[key])
    return array

def getInvoiceNumber(input):
    number = str(input)
    #print(type(input))
    #print(input)
    if type(input) is list:
        if input:
            number = str(input[0])
    return number

def getPrice(input):
    price = str(input)
    #print(type(input))
    #print(input)
    if type(input) is list:
        if input:
            price = str(input[-1])
    return price

def getCurrency(input):
    currency = str(input)
    #print(type(input))
    if type(input) is list:
        currency = str(input[-1])
    currency = currency.replace("€", "EUR")
    currency = currency.replace("$", "USD")
    return currency


if len(argv) > 1:
    pathname = argv[1]
else:
    pathname = input('pdf file path>>> ')

try:
    templates = read_templates("./templates/")

    if not os.path.exists(pathname):
        print("NOT EXIST")
        exit()

    if allowed_file(pathname):
        # print(pathname)
        # print(type(pathname))
        # print(type(templates))
        # print(read_template)
        # path_filename.append(pathname)
        # result = extract_data(pathname)

        result = extract_data(pathname, templates)
        # stz = get_localzone()
        # date_obj = date_obj.replace(tzinfo=stz)

        # if (not result):
        if (result == False):
            print('This PDF is currently not supported please make sure that you are using a orignal statment.')
            exit()

        #print(result)

        # result['date']=result['date'].strftime(DATE_FORMAT)
        #result['date'] = getDate(result['date'])
        result = exchangeDate(result, 'date')

        #result['sale_date'] = getDate(result['sale_date'])
        result = exchangeDate(result, 'sale_date')

        result = exchangeDate(result, 'subscription_date')

        result = exchangeInvoiceNumber(result, 'invoice_number')
        #result['invoice_number']=getInvoiceNumber(result['invoice_number'])

        result['currency']=getCurrency(result['currency'])

        result['amount']=getPrice(result['amount'])

        print(result)
        # pdfFiles.append(result)
        with open(pathname + ".json", 'w') as file:
            file.write(json.dumps(result))

        with open(pathname + ".date", 'w') as file:
            file.write(str(result['date']))

        with open(pathname + ".price", 'w') as file:
            file.write(str(result['amount']))

        with open(pathname + ".number", 'w') as file:
            file.write(str(result['invoice_number']))

        with open(pathname + ".currency", 'w') as file:
            file.write(str(result['currency']))

except FileNotFoundError:
    print(f'{argv[1]} not found')

except TypeError as error:
    print(error)
