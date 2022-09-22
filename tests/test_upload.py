import requests
import sys

url = 'http://127.0.0.1:8000/upload'
filename = sys.argv[1]
files = [('files', open(filename, 'rb')), ('files', open('images/2.png', 'rb'))]
resp = requests.post(url=url, files=files) 
print(resp.json())
