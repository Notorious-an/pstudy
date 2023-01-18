'''
내장 데이터 유형
-텍스트유형 str
-정수 유형 int, 실수 유형 float, 복소수 complex
-리스트 자료형 list, 튜플 tuple
  ex) list = [1,2,3,4]  tuple = (1,2,3,4)
-range 연속된 숫자를 가지고 있는 sequence type
-dictionary
  ex) x = {"name":"피카츄", "tech" : "electric"}
-set(집합)
  ex) x = {"피카츄", "꼬부기", "파이리"}
- bool(논리 type) : true, false 판별한다
- none type
  ex) none type
'''

'''
파이썬은 type를 자동으로 지정해서 저장한다
'''
# 숫자 + 숫자 = 숫자
# 문자 + 숫자 = 오류 (계산 안됨)
# 문자 + 문자 = 문자합쳐짐
num1 = 10
num2 = 20
result = num1 + num2
print(result)
name = 'Alice'
#result = name + num1
print(result)
age = '25'
result = name + '/' + age
print(result)