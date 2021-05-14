from flask import Flask

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import requests
from bs4 import BeautifulSoup
import time

app = Flask(__name__)

@app.route('/')
@app.route('/welcome')
def welcome():
    return '<h2>Welcome dear billion user!!!</h2>'

@app.route('/weather')
def get_weather():
    headers={
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
    }
    url = 'https://weather.com/uk-UA/weather/today/l/UPXX0486:1:UP?Goto=Redirected'
    
    req = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(req.text, 'lxml')

    weather = soup.find('div', class_='CurrentConditions--CurrentConditions--2_Nmm').text

    if weather == str(weather):
        return weather
    return 'f*ck'

# Python code to convert string to list character-wise
def Convert(string):
	list1=[]
	list1[:0]=string
	return list1

@app.route('/vin/<vin>')
def get_href(vin):
    if len(Convert(vin)) == 17:
        options = webdriver.ChromeOptions()

        options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36')
        # options.add_argument('--headless')

        driver = webdriver.Chrome(
            executable_path='webdriver/chromedriver',
            options=options
        )
        
        try:
            driver.get('https://autohelperbot.com/uk/login')


            # driver.find_element_by_xpath('/html/body/main/div[1]/div[1]/div[2]').click()

            WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "/html/body/main/div[1]/div[1]/div[2]"))).click()

            WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="email"]'))).send_keys('yarovlasenko@gmail.com')
            
            WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="email_auth"]/div/div/form/div[2]/input'))).click()

            WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="password"]'))).send_keys('12541254')


            WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH,'//*[@id="email_auth"]/div/div/form/div[5]/input'))).click()
            time.sleep(1)

            WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '/html/body/header/div/div/div[1]/a'))).click()


            WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="show_menu"]/div[2]/div/div/div/div[2]/a'))).click()


            WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="vin"]'))).send_keys(vin)

            WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '/html/body/main/div/div[1]/div/form/div[2]/input'))).click()
            time.sleep(1)

            req = requests.get(url=driver.current_url)
            
            return str(req.text)
        except Exception as ex:
            return str(ex)
        finally:
            driver.close()
            driver.quit()
    return 'Error(vin code must be at least 17 char)'
