import requests
import sys

url = 'http://127.0.0.1:8000/upload'
filename = sys.argv[1]
file = {'file': open(filename, 'rb')}
resp = requests.post(url=url, files=file) 
print(resp.json())
print('Cookies: ', resp.cookies)
