import requests
import json
'''
r = requests.get('https://api.github.com/eventsm')

print(r.json())
#print(r.content)
print(r)
'''

params = {"q":"白夜追凶"}
url = 'https://api.douban.com/v2/movie/search'
r = requests.get(url, params=params)

#print('Search Params:\n', json.dumps(params, ensure_ascii=False))
print('Search Response:\n', json.dumps(r.json(), ensure_ascii=False, indent=4))
print(r.json()["subjects"][0]['rating'])