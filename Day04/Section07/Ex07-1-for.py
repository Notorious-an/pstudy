'''
for 문
    값의 범위나 횟수가 정해져 있을 떄의 반복문
    while문 보다 훨씬 자주 사용된다.

for 변수 in 반복가능한 객체 :
    반복실행문
'''

pwd = 'abcdefg1234'
ch_count = 0
num_count = 0
for ch in pwd :
    if ch.isalpha():
        ch_count = ch_count + 1  # 문자의 개수를 세는 코드
    elif ch.isnumeric():
        num_count += 1  # 숫자의 개수를 세는 코드

if ch_count > 0 and num_count > 0 :
    print("가능한 비밀번호 입니다.")
else:
    print("불가능한 비밀번호 입니다.")