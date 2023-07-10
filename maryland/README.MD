# Реальная задача с ресурса UpWork

### в процессе решения задачи использовались библиотеки Selenium и Beautiful Soup

___

#### Описание


Hello,

I want to scrap the names of businesses and their addresses off
https://www.dllr.state.md.us/cgi-bin/ElectronicLicensing/OP_Search/OP_search.cgi?calling_app=HIC::HIC_business_location

It should be able to enter every zip code from Maryland when scraping and hitting each page.

Remove the bogus numbers infront of the address in the search results. Export all data for associated businesses into a .csv

___
### Для запуска

1. клонируем проект и переходим в папку maryland.
```
git clone git@github.com:DmitryZdor/scrapping_upwork.git

cd maryland
```
В проекте два основных скрипта maryland.py и main.py

2. Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv     
       или     
python -m venv venv
```
```
source venv/Scripts/activate
           или 
source venv/bin/activate           
```
3. Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

4. Запускаем maryland.py находясь в папке проекта maryland.
```
python maryland.py
```
по запросу вводим требуемый Zip Code например 21220  
Необходимый Zip Code List можно посмотреть на сайте https://www.ciclt.net/sn/clt/capitolimpact/gw_ziplist.aspx?zip=212

5.