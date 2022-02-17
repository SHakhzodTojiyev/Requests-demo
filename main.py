import requests

r = requests.get('https://xkcd.com/353/')

print(dir(r))
print(help(r))
print(r.status_code)
print(r.ok)
print(r.headers)
print(r.url)

# ******************************
# Just test 
r = requests.get('https://imgs.xkcd.com/comics/python.png')
with open('comic.png', 'wb') as f:
    f.write(r.content)
with open('comic.jpg', 'wb') as f:
    f.write(r.content)
