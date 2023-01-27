'''
함수 (function)
    하나의 특별한 목적의 작업을 수행하기 위해
    독립적으로 설계된 프로그램 코드의 집합.

def 함수이름(매개변수) :
    코드실행문
    return 반환값
'''

# welcome() 함수 정의   (함수를 정의만 하면 실행이 안됨)
# 매개변수도 return 값도 없는 함수
def welcome() :   # 여기서 함수를 정의하고
    print('Hello python')
    print('Nice to meet you')

welcome()  # 여기서 호출하는 것이다.
           # welcome 함수에 print 문이 있어서 출력되는 것!!

# 매개변수 있으나, return 값이 없는 함수

def introduce(name, age) :  # 함수내에서 사용할 매개변수가 2개인 함수 정의
    print('내이름은 {}이고, 나이는 {}살 입니다.'.format(name, age))

introduce('안병수', 38)

# 매개변수가 가변적인 함수

def show(*args) :  # 함수내에서 사용할 매개변수 개수가 가변적인 함수 정의
    for item in args :    #여기서 args는 튜플이다.
        print(item)
show('python')
show('python', 'java', 'C++')

# 매개변수는 없고, 반환 값(return)이 있는 함수
def address() :
    str = '우편번호 12345\n'
    str = str + '서울시 영등포구 여의도동'
    return str

result = address()
print(result)

# 매개변수 있고, return이 있는 함수

def plus(num1, num2) :
    return num1 + num2

result = plus(3, 5)
print(result)

# 함수 바깥에 있는 변수를 가져와서 수정하고 싶으면 global 변수 선언해줘야 함
area = 0
def rmove() :
    global area  # 함수바깥에 있는 변수 가져와서 수정하고 싶으면 글로벌 선언 해줌
    area += 1

def lmove() :
    global area  # 함수바깥에 있는 변수 가져와서 수정하고 싶으면 글로벌 선언 해줌
    area -= 1

rmove()
rmove()
lmove()
print('유닛이 오른쪽으로 {}칸 이동했습니다.'.format(area))