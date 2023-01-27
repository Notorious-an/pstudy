'''
내장함수 보충
'''

# format
result = format(10000) # str(10000)과 같다
print(type(result))
result = format(10000, ',') # 천단위 쉼표
print(result)

#abs 절대값

result = abs(10)
print(result)
result = abs(-10)
print(result)

# max 최대값 반환
result = max(1,10)
print(result)
list1 = [5,6,3,1,4,10]
print(max(list1))

# min 최소값 반환
result = min(1,10)
print(result)
list1 = [5,6,3,1,4,10]
print(min(list1))

# pow() 거듭제곱

result = pow(10, 2) # 10의 거듭제곱
print(result)


# sorted() 함수 - 정렬
my_list = [1,3,4,5,3,7,8]
result = sorted(my_list)  # 순정렬
print(result)
result = sorted(my_list, reverse = True) # 역정렬 때리기
print(result)

# zip() 함수 - 같은 인덱스 번호끼리 튜플로 묶어 준다

names = ['james','emily','amanda']
score = [60, 40, 50]

for student in zip(names, score) :  # 같은 인덱스 번호끼리 튜플형태로 묶어버린다
    print(student)

for name, score in zip(names, score) :
    print('{}의 점수는 {}점 입니다.'.format(name, score))


