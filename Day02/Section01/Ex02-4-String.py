'''
문자열(String)
    하나 이상 연속된 문자(character)들의 나열
    파이썬에서 문자열 자료형은 큰따옴표(" ")
    또는 작은 따옴표( ' ' ) 사이에 위치한다
'''
# 'hello' = "hello" 는 동일
print('Hello' == "Hello")  # 같으면 True 반환

'''
여러줄 문자열
    세개의 따옴표를 사용하여 변수에 여러줄 문자열 할당
'''
a = """피카츄, 라이츄, 파이리, 꼬부기
버어플, 야도란, 피존투, 또가스
"""
print(a)

'''
문자열 인덱싱(indexing)
 H   E   L   L   O  <== 문자열
 0   1   2   3   4  <== 인덱스
-5  -4  -3  -2  -1  <== 마이너스 인덱스
'''
a = "Hello"
print(a[1]) # 정답은 e  앞에서 부터 0 1
print(a[-4]) # 정답은 e  뒤에서 부터 -1 -2 -3 -4


'''
문자열 슬라이싱(slicing)
  슬라이스 구문을 사용하여 문자 범위를 반환할 수 있다.
  문자열의 일부를 반환하려면 시작 인덱스와 끝 인덱스를 콜론으로 구분한다
'''
b = "Hello, World"
print(b[2:5]) # 정답은 llo, 2~4까지를 의미한다
print(b[:5]) # 정답은 Hello, 처음부터 4까지를 의미한다
print(b[2:]) # 정답은 llo, World, 3부터 끝까지를 의미한다

'''
대문자(Upper), 소문자(lower), 대체(Replace)
문자 단순히 합치기 (a+b)
'''
aa = "Python"
b = "Hello, World"
print(b.upper()) # 전부 대문자로 바꾸기
print(b.lower()) # 전부 소문자로 바꾸기
print(b.replace("H","J")) # 특정 문자 바꾸기
c = aa + ' ' + b # 공백입력하여 합치기
print(c)