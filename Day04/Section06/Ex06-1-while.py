'''
반복문 : 어떤 수행 작업을 한번이 아니라 계속해서 수행해야 할 떄 사용한다.
반복문 종류
  - while, for 문

while문
    특정 조건을 만족하는 동안 반복해서 수행하는 코드
while 조건식 :
    반복 실행 코드
'''

n = 10
while n > 1 :
    print(n)
    n = n - 1 # n -= 1 와 같다

print("while 끝나고 n 값 : {}".format(n))


# 반복문 나가고 싶을 때 쓰는 탈출하는 코드 break

coffee = 10
money = 300
while money :
    print("돈 받았으니 커피를 줍니다")
    coffee = coffee - 1
    print("남은 커피량은 {}개 입니다.".format(coffee))
    if coffee == 0 :
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break


# 10 이하 중 홀수만 출력하기 continue 사용법

a = 0
while a < 10 :
    a = a + 1
    if a % 2 == 0 : # a가 짝수이면
        continue  # while로 돌아가라
    print(a)