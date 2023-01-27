
# join() 메소드 : 특정 기준으로 합쳐서 문자열로 반환하는 메소드
s = '-'.join('python')
print(s)

s = '+'.join(['a','b','c','d'])
print(s)

# split() 메소드 : 기준으로 잘라서 list로 반환하는 메소드
s = 'Life is too short'
result = s.split()
print(result)

s = '010-2221-3437'
result = s.split('-')
print(result)

data = '안병수|38|산업은행'
result = data.split('|')
print(result)


# replace() 메소드 - 문자열을 치환하는 메소드
s = 'life is too short'
result = s.replace('short','long')
print(result)

# strip(), lstrip(), rstrip() 공백제거 하는 메소드
s = '          apple'
result = s.lstrip()  # lstrip 왼쪽 공백 제거
print(result)
s = 'apple       '
result = s.rstrip()  # rstrip 왼쪽 공백 제거
print(result)

s = '     apple       '
result = s.strip()  # 양쪽 공백 제거
                    # 참고로 문자열 중간 공백은 특정의미가 있다고 보고 제거 불가능
print(result)

s = ' app  le  '
result = s.strip() # 참고로 문자열 중간 공백은 특정의미가 있다고 보고 제거 불가능
print(result)

# ** 중간 값 제거하는 방법 **
# replace로 바꿔줘 버리자

s = ' app le  '
result = s.strip()
result1 = result.replace(' ','')  #중간 공백은 replace를 활용해서 제거하자
print(result1)

