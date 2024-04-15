"""
1.	Скачать Postman. Используя один из предложенных API,
или свой API, получить информацию о данном API

import requests
from requests import request

response = requests.get('https://v2.jokeapi.dev/info')
print(response.status_code)
print(response.json())

2.	Используя requests вывести информацию об каком-то одном instance.

import requests
from requests import request

response = requests.get('https://v2.jokeapi.dev/joke/Any')
print(response.status_code)
print(response.json())

3.	Получить данные из API, отсортировав их по какому-либо признаку.
Например, если вы используете API для получения новостей покажите только
новости определенной категории или из определенного источника.

import requests
api_key = 'd492e9ef1a904617946821040ff0687c'
category = 'business'
url = f'https://newsapi.org/v2/top-headlines?country=ru&category={category}&apiKey={api_key}'

response = requests.get(url)
print(response.status_code)
data = response.json()

for article in data['articles']:
    print(article['title'], article['source']['name'])

4.	Проанализируйте ваше API. Например: извлеките определенные данные из ответа
( получите заголовки новостей из JSON-ответа и вывести их на экран).

import requests
api_key = 'd492e9ef1a904617946821040ff0687c'
category = 'business'
url = f'https://newsapi.org/v2/top-headlines?country=ru&category={category}&apiKey={api_key}'

response = requests.get(url)
print(response.status_code)
data = response.json()

response = requests.get(url)
data = response.json()

for article in data['articles']:
    print(article['title'])
"""
