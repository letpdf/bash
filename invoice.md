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
python3 pdf2txt.py "/media/tom/projects/softreck-invoices/2020/07.2020/namecheap/namecheap-order-58819941.pdf"
python3 pdf2txt.py "/media/tom/projects/softreck-invoices/2020/06.2020/ovh/Invoice_IE747123.pdf"
python3 pdf2txt.py "/media/tom/projects/softreck-invoices/2020/02.2020/ovh/Invoice_IE697171.pdf"
python3 pdf2txt.py "/media/tom/projects/softreck-invoices/2020/12.2020/aftermarket/Faktura_FP_506_12_2020.pdf"
python3 pdf2txt.py "/media/tom/projects/softreck-invoices/2020/11.2020/mserwis/faktura_617_11_2020.pdf"
python3 pdf2txt.py "/media/tom/projects/softreck-invoices/2020/11.2020/modulesgarden/modulesgarden-Invoice-67310.pdf"
python3 pdf2txt.py "/media/tom/projects/softreck-invoices/2020/12.2020/modulesgarden/Invoice-2020_5259_MG.pdf"
python3 pdf2txt.py "/media/tom/projects/softreck-invoices/2020/12.2020/universal/faktura-fr-06-12-2020.pdf"

