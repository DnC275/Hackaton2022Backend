import requests
import sys

TOKEN='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZWRpYV91aWRzIjpbIjU5M2UwZmRjNTkwZDQ2MmI4OTI1OTRiOGZlMDMwMjEzIiwiMGJmMTNhNGU0ZDdmNDA1NmEwMGViNjhhZTljOWM0NTYiLCJlZTAyMWI0ZTM0MGM0MWI3OWEyMzRkZDFkZGQxZGRiMiIsIjk4YWMwNDA2MmIzNjRjNmI5ZjAzMjkxYTNmZTljMGZmIiwiOWU3MjUxMDNhYWUwNDRhYmI2YTRiNDIwOWYyYWY2Y2MiLCI1OWIwYWUzOWE0NmQ0MTI0OWJjYzQyZmNmMjA3MTIxOSIsImZlN2ZiYmRlNzNjYjRiYmY5MDFlZTJlMjg4MjA4MTk2IiwiNDI5MTM2ZTMyOTViNDliMjkxMzA2YjFkMjhlM2UzMzMiLCJiMmM5OTE0ZWQzYzg0MzJkODJhZWVmNmVkNzRiMTE4MSJdfQ.-o_epAEycAliT_7xGaRlPFIIJ_SaBwWi7b5_whZpM-k'
# url = 'http://127.0.0.1:8000/process'
url = 'http://ahahaton3022.huiso.su/api/process'
# url = 'http://ahahaton3022.vantus-software.ru/api/process'
data = {
    'fragments': [
        {
            'video_id': '376d76818d934fb19c2f8a79972a539a',
            'begin': 0,
            'end': 10
        }
    ],
    'format': '.mp4'
}
resp = requests.post(url=url, json=data, cookies={'token': TOKEN})
print(resp)
print(resp.json())
print('Cookies: ', resp.cookies)
{"fragments": [{"video_id": "376d76818d934fb19c2f8a79972a539a","begin": 0,"end": 10}],"format": ".mp4"}
