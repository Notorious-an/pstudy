'''
divmod() 함수
    두 숫자를 인자로 전달 받아
    첫번쨰 인사를 두번쨰 인자로
    나는 몫과 나머지를 Tuple 형식으로 반환한다.
'''

money = 10000
price = 3000
result = divmod(money, price)  # result = 3, 1000 을 출력했음
print('빵을 {}개 사고, {}원이 남았습니다.'
      .format(result[0], result[1]))
