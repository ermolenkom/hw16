from concurrent.futures import ThreadPoolExecutor, as_completed

import json
import requests
from datetime import datetime
  
f = open('photos.json')
data = json.load(f)

def download(json_elm):
    url = json_elm.get("url").replace("https://", "http://")
    file_name = "output/"+str(json_elm.get("id")) + ".jpg"
    #urllib.request.urlretrieve(url, file_name)
    header = { 
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'DNT': '1',
'Host': 'via.placeholder.com',
'If-Modified-Since': 'Wed, 30 Dec 2020 01:00:11 GMT',
'If-None-Match': '"5febd11b-875"',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',    
}
    session = requests.Session()
    session.headers = header
    img_data = session.get(url)

#    img_data=requests.get(url, headers=header)
    if img_data.status_code != 403:
        with open(file_name, 'wb') as handler:
            handler.write(img_data.content)

    url = json_elm.get("thumbnailUrl").replace("https://", "http://")
    file_name = "output/"+str(json_elm.get("id")) + "_t.jpg"
    session = requests.Session()
    session.headers = header
    img_data = session.get(url)
    if img_data.status_code != 403:
        with open(file_name, 'wb') as handler:
            handler.write(img_data.content)
    return file_name        


start_time = datetime.now()
with ThreadPoolExecutor(max_workers=1) as executor:
    futures = [executor.submit(download, item) for item in data]
    for future in as_completed(futures):
#        try:
            print(future.result())
#        except Exception as exc:
#            print(exc)
print(datetime.now() - start_time)
