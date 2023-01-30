'''
파일명

별명 사용하기
'''

import converter as cvt  # 모듈 이름이 길때는 별칭을 써서 활용한다.

miles = cvt.kilometer_to_miles(150)
print('150km = {}miles'.format(miles))

pounds = cvt.gram_to_pounds(1000)
print('1000g = {}pounds'.format(pounds))
