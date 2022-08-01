#!/usr/bin/python3

import pandas as pd
import numpy as np
import re
import time

import requests
from bs4 import BeautifulSoup
import csv

# Сделаем сразу единую таблицу, для работы (чтобы с ней работать над пропусками, новыми фичами и т.д.)

# вот так можно бороться с тем, что просто скачивание из Google Drive по обычной ссылке не получается
url_main='https://drive.google.com/file/d/1bfGQ_OVPj1N3TKdW4l6a78CQFihEyYhp/view?usp=sharing'
url_kaggle= 'https://drive.google.com/file/d/1xU6EZs5BeMRfyt8hp1uNpZBy2JCKn7w7/view?usp=sharing'

url_main='https://drive.google.com/uc?id=' + url_main.split('/')[-2]
url_kaggle='https://drive.google.com/uc?id=' + url_kaggle.split('/')[-2]

data_main = pd.read_csv(url_main)
data_kaggle = pd.read_csv(url_kaggle)

# Добавим признак 'Main' для отделения основной выборки от валидационной
data_main['Main'] = True
data_kaggle['Main'] = False

# объединим в одну табличку
data = pd.concat([data_main, data_kaggle])

# добавим столбец с полной ссылкой на ресторан
data['URL_TA_full'] = 'https://www.tripadvisor.com' + data['URL_TA']


# Напишем несколько функций

def get_soup(url):
  """на вход ссылка
     имитируем поведение браузера, иначе трипэдвайзер не отдает данные
     возвращаем объект - 'супчик'
  """
  
  headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
            #'User-Agent': '*',
             'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
             'Accept-Language': 'en-US,en;q=0.5',
             'Accept-Encoding': 'gzip, deflate',
             'Connection': 'keep-alive',
             'Upgrade-Insecure-Requests': '1',
            }
  
  try:
    s = requests.Session()
    s.headers.update(headers)
    r = s.get(url,allow_redirects=False)
  except:
    return 0
    
  if r.status_code != 200:
    return 0
  else:
    return BeautifulSoup(r.text, 'html.parser')

def make_features(url, soup):
      """
      в этой функции будем собирать нужные нам данные с сайта трипэдвайзер
      """
      features = {}
      if soup == 0:
            features[url] = {}
            features[url]['alive'] = 0
            return features

      else:
            features[url] = {}
            features[url]['alive'] = 1

            #price_range
            try:
              features[url]['price_range'] = soup.find_all('a', class_="drUyy")[0].text
            except:
              features[url]['price_range'] = np.nan
            
            #cuisines
            try:
              features[url]['cuisines'] = []
              for cuisine in soup.find_all('a', class_="drUyy")[1:]:
                    features[url]['cuisines'].append(cuisine.text)
            except:
              features[url]['cuisines'] = np.nan

            #reviews
            try:
              features[url]['reviews'] = soup.find('span', class_="eBTWs").text.split(' ')[0]
            except:
              features[url]['reviews'] = np.nan

            #rating
            try:
              features[url]['rating'] = soup.find('span', class_="fdsdx").text
            except:
              features[url]['rating'] = np.nan

            #mean_check
            try:
              features[url]['mean_check'] = soup.find('div', class_="cfvAV").text
            except:
              features[url]['mean_check'] = np.nan

            #quality reviews (Excelent, Very good, Average, Poor, Terrible)
            try:
              features[url]['excelent'] = soup.find_all('span', class_="row_num is-shown-at-tablet")[0].text
            except:
              features[url]['excelent'] = np.nan
            try:
              features[url]['very_good'] = soup.find_all('span', class_="row_num is-shown-at-tablet")[1].text
            except:
              features[url]['very_good'] = np.nan
            try:
              features[url]['average'] = soup.find_all('span', class_="row_num is-shown-at-tablet")[2].text
            except:
              features[url]['average'] = np.nan
            try:
              features[url]['poor'] = soup.find_all('span', class_="row_num is-shown-at-tablet")[3].text
            except:
              features[url]['poor'] = np.nan
            try:
              features[url]['terrible'] = soup.find_all('span', class_="row_num is-shown-at-tablet")[4].text
            except:
              features[url]['terrible'] = np.nan

            #ranking позиция среди ресторанов в данном городе
            try:
              features[url]['ranking'] = []
              for place in soup.find_all('div', class_="fYCpi"):
                    features[url]['ranking'].append(place.text)
            except:
              features[url]['ranking'] = np.nan

      return features




while True:
    try:
        length = pd.read_csv(r'parsed.csv').shape[0]
        if length + 100 >= 50000: #последний блок
          restaurants = {}
          for path in data['URL_TA_full'].iloc[length:50000]:
              restaurant = make_features(path, get_soup(path))
              restaurants = {**restaurants, **restaurant}
              time.sleep(2)
          df_parse = pd.DataFrame.from_dict(restaurants, orient='index')
          df_parse['URL_TA_full'] = df_parse.index
          df_parse.to_csv(r'parsed.csv', mode='a', index=False, header=False)
          break
        print(length)
        restaurants = {}
        for path in data['URL_TA_full'].iloc[length:length+100]:
            restaurant = make_features(path, get_soup(path))
            restaurants = {**restaurants, **restaurant}
            time.sleep(2)
        df_parse = pd.DataFrame.from_dict(restaurants, orient='index')
        df_parse['URL_TA_full'] = df_parse.index
        df_parse.to_csv(r'parsed.csv', mode='a', index=False, header=False)
    except:
        print(length)
        restaurants = {}
        for path in data['URL_TA_full'].iloc[0:100]:
            restaurant = make_features(path, get_soup(path))
            restaurants = {**restaurants, **restaurant}
            time.sleep(2)
        df_parse = pd.DataFrame.from_dict(restaurants, orient='index')
        df_parse['URL_TA_full'] = df_parse.index
        df_parse.to_csv(r'parsed.csv', index=False)

    length = pd.read_csv(r'parsed.csv').shape[0]
    if length >=50000:
        break

