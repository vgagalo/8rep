from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import time

def weather():
    headers={
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
    }
    url = 'https://weather.com/uk-UA/weather/today/l/UPXX0486:1:UP?Goto=Redirected'
    
    req = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(req.text, 'lxml')

    weather = soup.find('div', class_='CurrentConditions--CurrentConditions--2_Nmm')
    print(weather.text)