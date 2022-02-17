import requests

auth = ('shakhzod', 'testing')
r = requests.get('https://httpbin.org/basic-auth/shakhzod/testing', auth=auth)

print(r.text)