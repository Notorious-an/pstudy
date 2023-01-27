'''
메소드(Mothod)란?
    특정객체가 가지고 있는 함수를 의미한다.
    객체.메소드() 사용가능

 STR에서 사용가능한 메소드
'''

# String 객체 format 메소드
print("10자리 폭 왼쪽 정렬 '{:<10d}'".format(123))
print("10자리 폭 오른쪽 정렬 '{:>10d}'".format(123))
print("10자리 폭 가운데 정렬 '{:^10d}'".format(123))
print()
# 해석하자면
# 123을 넣으면 ' ' 때문에 str으로 인식되고, str 객체에 있는 format 메소드 사용가능

print("10자리 폭 왼쪽 정렬 채움문자 '{:*<10d}'".format(123))
print("10자리 폭 오른쪽 정렬 채움문자 '{:*<10d}'".format(123))
print("10자리 폭 가운데 정렬 채움문자 '{:*^10d}'".format(123))

# count() 메소드
s = '내가 그린 기린 그림은 긴 기린 그림이고, 네가 그린 기린 그림은 목 짧은 기린 그림이다.'
result = s.count('기린')
print(result)  # 정답은 4

s = 'best of best'
result = s.count('best', 5)  # 5라는 매개변수는 5번째 인덱스부터 찾으라는 뜻
print(result)

# find() 메소드 : 위치한 인덱스 번호 반환
s = 'apple'
result = s.find('p')
print(result)

result = s.find('z')   #없는 값이 나왔을떄는 -1 값을 반환한다.
print(result)
if result == -1 :
    print('존재하지 않는 문자입니다.')

s = 'best of best'
result = s.find('best',5)
print(result)
result = s.find('best', -7)   # 인덱스를 -형태로 셀수도 있다 -8 -7 -6... -1
print(result)

# (-) 인덱스 활용하기
# ' b  e  s  t  o  f  b  e '
#  -8 -7 -6 -5 -4 -3 -2 -1

# index() : find() 메소드와 같지만 문자열이 존재하지 않을 경우 에러 발생!!
s = 'apple'
result = s.index('p')
print(result)

# result = s.index('z') # 문자열이 없어서 에러 발생
# print(result)

