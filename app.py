import json
import requests


# GET
# payload = {'page': 2,'count': 25}
# r = requests.get('https://httpbin.org/get', params=payload)


# ********************************
payload = {'username': 'shakhzod','password': 'testing'}
r = requests.post('https://httpbin.org/post', data=payload)

# print(r.url)
# print(r.text)
# print(r.json())

r_dic = r.json()

print(r_dic['form'])