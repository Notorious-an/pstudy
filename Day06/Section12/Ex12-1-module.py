'''
모듈(Module)
    변수나 함수 또는 클래스를 모아 놓은 파일을 모듈이라고 한다.

    모듈사용법 import 모듈명
    -> 남들이 만들어 놓은 module을 가져다 쓸 수 있다.

'''

import converter  # 앞서서 만들어놓은 함수를 불러올 수 있다.

miles = converter.kilometer_to_miles(150)
print('150km = {}miles'.format(miles))

pounds = converter.gram_to_pounds(1000)
print('1000g = {}pounds'.format(pounds))
