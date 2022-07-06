from sys import argv
from invoice2data import extract_data
from invoice2data.extract.loader import read_templates
import json
import os

ALLOWED_EXTENSIONS = set(['pdf'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def currency_data_to_float(ammount):
    return float(ammount.replace(',', '').replace('$', ''))

if len(argv) > 1:
    pathname = argv[1]
else:
    pathname = input('pdf file path>>> ')

try:
    templates = read_templates("invoice_templates/")

    #if pathname.endswith(".pdf"):
    if os.path.exists(pathname):
        print("EXIST")
    else:
        print("NOT EXIST")

    if pathname.endswith(".pdf") and allowed_file(pathname):
        print(pathname)
        #print(type(pathname))
        #print(type(templates))
        #print(read_template)
        #path_filename.append(pathname)
        result = extract_data(pathname, templates=templates)

        if (not result):
            print('This PDF is currently not supported please make sure that you are using a orignal statment.')

        exit()

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

except FileNotFoundError:
    print(f'{argv[1]} not found')

except TypeError as error:
    print(error)

