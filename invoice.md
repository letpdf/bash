# invoice

## załadowanie przez email
/invoice/in

## załadowanie bezpośrednio do folderu
/invoice in

## uruchomienie

codzienne sprawdzanie zawartości

./invoice.sh


## Usage

./invoice.sh ionos_2020 2020
./invoice.sh ionos_2021 2021

## Dependencies

git clone "https://github.com/letpdf/templates" "templates"

## regexp 

./pdf2txt.sh "/media/tom/projects/softreck-invoices/2020/03.2020/strato/DRP78923200.pdf"

python3 pdf2txt.py "/media/tom/projects/softreck-invoices/2020/03.2020/strato/DRP78923200.pdf"
