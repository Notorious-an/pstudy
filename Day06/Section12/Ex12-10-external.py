'''
패키지
    모듈의 상위 개념
    모듈의 집합을 의미한다.

    모듈(파이썬 파일)을 모아놓은 것!!

패키지 설치 방법
console> pip install package 명

패키지 삭제 방법
console> pip uninstall package 명
'''

# 행렬 연산 관련 package
import numpy as np

print(np.sum([1,2,3,4,5]))
a = np.array([1,2,3])
b = np.array([4,5,6])

# 각 요소 더하기
c = a + b
c = np.add(a,b)
print(c)

# 각 요소 빼기
c - a - b
c = np.subtract(a, b)
print(c)

# 각 요소 나누기
c - a / b
c = np.divide(a, b)
print(c)

# 각 요소 곱하기
c - a * b
c = np.multiply(a, b)
print(c)

