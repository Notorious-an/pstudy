'''
파일명 Ex02-2-variable.py  변수에 대해서 학습
변수(variable)  : 어떤 데이터를 저장하고자 할 떄 사용하는 메모리 저장소
변수명 규칙
    영문, 한글, 숫자, 밑줄(_)로 구성된다.
    특수문자(!@#!@$) 사용할 수 없다!!
    대문자와 소문자를 구분한다(다른 문자로 인식)
    변수명의 첫 글자를 숫자로 사용할 수 없다
    키워드(list, dict, if, for, and 등 명령어)는 변수로 사용할 수 없다.
'''

name = 'Alice'  # 문자열 변수
print(name)
age = 25 # 숫자 변수
print(age)
addressds = '''우편번호 1234
서울시 영등포구 여의도동 123-45
'''
print(addressds)

''' 변수를 잘못 사용한 예시 '''
# (꿀팁) Ctrl + /   주석 단축키를 의미함
# 줄복사를 하려면 Crtl + D (엑셀처럼 가능)

# 2mybar = 'Python1'
# my-var = 'Python2'
# my var = 'Python3'

''' 여러값을 한번에 할당 할 수 있음'''
# 튜플형식이라고 이해하면됨
x, y, z = "피카츄", "꼬부기", "파이리"
print(x)
print(y)
print(z)