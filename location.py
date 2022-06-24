
#from dotenv import load_dotenv
from pathlib import Path
import csv
from bs4 import BeautifulSoup
import re
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed


#from sendemail import f_sendemail

#load_dotenv()

url_wiki = "https://en.wikipedia.org/wiki/List_of_cities_in_Canada"
url_coord = "https://nominatim.openstreetmap.org/"

def get_coord(city: str) -> list:
    '''Получение координат города'''
    params = {"addressdetails": 1, "q": city, "format": 'json', "limit": 1}
    response = requests.get(url_coord, params=params)
    return [str(response.json()[0].get("lat")),str(response.json()[0].get("lon")),city]

def make_csv() -> None:
    '''Подготовка csv-файла'''
    citys = []
    response = requests.get(url_wiki)
    if response.status_code == 200:
        all_tables = BeautifulSoup(response.text, "html.parser").findAll("table",{"class": "wikitable"})
        with open("city.csv", "w", newline='', encoding='utf-8') as out:
            w = csv.writer(out, delimiter = ';')   
            for table in all_tables :
                if len(table) > 1:
                    rows = table.find_all('tr')
                    for row in rows[0:]:
                        cells = row.find_all('td',{"scope": "row"})
                        if len(cells) > 0:
                                city = re.sub("[\(\[].*?[\)\]]", "", cells[0].text.strip())
                                citys.append(city)    

            with ThreadPoolExecutor(max_workers=2) as executor:
                futures = [executor.submit(get_coord, item) for item in citys]
                for future in as_completed(futures):
                    try:
                        crd = future.result()
                    #    print(crd[2]+" "+str(crd[0])+" "+ str(crd[1]))  
                        w.writerow([crd[2], str(crd[0]), str(crd[1])])
                    except Exception as exc:
                        print(exc)
                            

def f_location(email:str):
    """
    Создает csv файл для списка городов в Канаде(смотри таблицы в https://en.wikipedia.org/wiki/List_of_cities_in_Canada) вида:city,lat,lon (город, широта, долгота)
 https://nominatim.org/release-docs/develop/api/Overview/ - здесь можно получить широту и долготу
Результаты отправляет на почту преподавателя с помощью средств python
    """
    make_csv()

   # filename = Path("city.csv").absolute()
   # subject = "Cписок городов в Канаде"
   # f_sendemail(email, subject, subject, filename) 
