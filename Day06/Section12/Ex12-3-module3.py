'''
모듈 사용법

from 모듈명 import 함수
from 모듈명 import 함수1, 함수2
from 모듈명 import *
'''

from converter import *

miles = kilometer_to_miles(150)  # converter.kilometer_to_miles 아니고, 바로 함수 쓰면 된다.
print('150km = {}miles'.format(miles))

pounds = gram_to_pounds(1000)
print('1000g = {}pounds'.format(pounds))
