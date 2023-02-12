
'''
request 모듈 설치
pip install requests
'''

import requests

url = 'https://movie.naver.com/movie/bi/mi/basic.nhn'
param = {'code': 161967}
response = requests.get(url,params=param) #request get 메소드를 통해 url 주소의 papameter 기준으로 html 가져옴
print(response.text)