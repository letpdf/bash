# pdf to text 

invoice data


## Install on linux

sudo apt-get install python3-pip
sudo pip3 install virtualenv

## Prepare Python project
virtualenv venv
source venv/bin/activate

## Python dependencies

pip install Flask
pip install pymongo
pip install invoice2data


## start

```bash
python3 pdf2txt.py "/media/tom/projects/softreck-invoices/2020/01.2020/ionos/"
```


```bash
python3 pdf2txt.py "/media/tom/projects/softreck-invoices/2020/06.2020/ovh/"
```
```bash
python3 pdf2txt.py "/media/tom/projects/softreck-invoices/2020/01.2020/strato/"
```


```bash
python3 pdf2txt.py "/media/tom/projects/softreck-invoices/2020/01.2020/premium/"
```

```bash
python3 pdf2txt.py "/media/tom/projects/softreck-invoices/2020/03.2020/strato/"
python3 pdf2txt.py "/media/tom/projects/softreck-invoices/2020/01.2020/websouls/"
python3 pdf2txt.py "/media/tom/projects/softreck-invoices/2020/06.2020/whmcs/"
python3 pdf2txt.py "/media/tom/projects/softreck-invoices/2020/09.2020/mserwis/"
python3 pdf2txt.py "/media/tom/projects/softreck-invoices/2020/05.2020/namesilo/"
python3 pdf2txt.py "/media/tom/projects/softreck-invoices/2021/06.2021/ionos/"
python3 pdf2txt.py "/media/tom/projects/softreck-invoices/2021/06.2021/strato/"
python3 pdf2txt.py "/media/tom/projects/softreck-invoices/2020/in_2020/"
python3 pdf2txt.py "/media/tom/projects/softreck-invoices/2020/04.2020/premium/"
```
/media/tom/projects/softreck-invoices/2021/06.2021/ionos/RG_100087501113.pdf
2020/01.2020/websouls/Invoice-96274.pdf

```bash
python3 pdf2txt.py "/media/tom/projects/softreck-invoices/2020/01.2020/ionos/"
```
#python3 pdf2txt.py "/media/tom/projects/softreck-invoices/2020/01.2020/ionos/RG100067031335-sig.pdf"