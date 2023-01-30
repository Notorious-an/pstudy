'''
지역변수(local)
    함수 내부 선언
    함수 내부에서만 사용가능

전역변수(global)
    함수 외부 선언
    함수 내부 외부 모두 사용가능
'''


gVar = '전역'
def globalAndLocal():
    lVar = '지역'
    print(gVar, '변수 입니다.')  # 전역변수를 참조만 가능하고, 함수안에서 수정은 안된다.
    print(lVar, '변수 입니다.')

globalAndLocal()


gVar = '전역'
def globalAndLocal2():
    lVar = '지역'
    gVar = '변경된 전역이 아닌 새로운 지역'
    print(gVar, '변수 입니다.') # 여기서 출력된 변수는 지역변수이다. 전역변수를 사용하려면 글로벌 선언 해줘야 함
    print(lVar, '변수 입니다.')

globalAndLocal2()
print(gVar)

# 전역변수 선언하기

total = 0
def gift(dic, who, money):
    global total # 전역변수 total을 사용하겠다.
    total = total + money
    dic[who] = money  # 딕셔너리에 하나씩 추가함
    # 딕셔너리는 글로벌 선언 안해줘도 됨, 딕셔너리는 주소값을 가지고 있다 그래서 값 수정이 가능하다
    # 정수, 실수 등 immutable 변수는 글로벌 선언을 해줘야 한다, 아니면 참조만 가능하다

wedding = {}
gift(wedding, '영희', 5)
gift(wedding, '철수', 10)
gift(wedding, '이모', 10)

print('축의금 명단 : {}'.format(wedding))
print('전체 축의금 : {}'.format(total))
