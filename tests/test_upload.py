import requests
import sys

url = 'http://127.0.0.1:8000/upload'
filename = sys.argv[1]
file = {'file': open(filename, 'rb')}
resp = requests.post(url=url, files=file, cookies={'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZWRpYV91aWRzIjpbIjRhZjE1M2M2YjhkYzRiMDJiZTIzM2E1YjZjZWY0NTFmIl19.XGuwjQBuUiVPaVmghW_dbLAvTdWJEYNQHGwrDKEH_RM'})
print(resp.json())
print('Cookies: ', resp.cookies)
