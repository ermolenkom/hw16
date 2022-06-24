import requests
from dotenv import load_dotenv

from sendemail import f_sendemail
import os
load_dotenv()

def f_rate(curr: str) -> str:
    '''Запрос к Api'''
    api_key = os.getenv("Api-Key")
    url = os.getenv("url") 
    params = {"get": "rates", "pairs": curr, "key": api_key}
    response = requests.get(url, params=params).json()
    return "Курс валюты "+ curr + " = "+response.get("data", {}).get(curr)
    
def f_currency(email:str):
    """
    Функция будет работать с внешним API для получения курса валют для выбранной     динамически валюты
Результаты отправить на почту преподавателя с помощью средств python
    """    
    curr = input("Введите валюту, например USDRUB: ")
    if curr:
        subject = "Курс валюты"
        f_sendemail(email, subject, f_rate(curr), None) 


