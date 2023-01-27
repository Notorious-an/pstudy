'''
집합 연산하는 mothod에 대해서 알아보자
'''


# 교집합 intersection()
s1 = {'apple', 'orange', 'banana'}
s2 = {'apple', 'banana', 'cherry'}
print(s1&s2) # 연산자로 계산하는 법
result = s1.intersection(s2) # intersection 메소드로 사용하기
print(result)

# 합집합 union()
s1 = {'apple', 'orange', 'banana'}
s2 = {'apple', 'banana', 'cherry'}
print(s1 | s2) # 연산자로 계산하는 법
result = s1.union(s2) # intersection 메소드로 사용하기
print(result)

# 차집합 difference()
s1 = {'apple', 'orange', 'banana'}
s2 = {'apple', 'banana', 'cherry'}
print(s1-s2) # 연산자로 계산하는 법
result = s1.difference(s2) # intersection 메소드로 사용하기
print(result)