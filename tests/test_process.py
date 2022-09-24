import requests
import sys

url = 'http://127.0.0.1:8000/process'
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
resp = requests.post(url=url, json=data, cookies={'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZWRpYV91aWRzIjpbIjRhZjE1M2M2YjhkYzRiMDJiZTIzM2E1YjZjZWY0NTFmIiwiMzc2ZDc2ODE4ZDkzNGZiMTljMmY4YTc5OTcyYTUzOWEiXX0.J84ZQFy97JwCNROsyfrLVdkRoLaoWdYTmlhZIW1tafI'})
# print(resp.json())
print('Cookies: ', resp.cookies)
