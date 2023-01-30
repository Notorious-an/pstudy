'''

[회원가입]
아이디를 입력하세요(3글자 이상) :
3글자 이상 입력이 아닌경우 -> 3글자 이상 입력하세요

아이디를 입력하세요(3글자 이상) : (이거 다시 뜨기)

패스워드를 입력하세요 (영문 숫자 포함 8자 이상) :
아닌 경우  : 영문 숫자 포함 8자이상 입력해 주세요!

패스워드 확인  : 한번 더 입력하세요
틀린경우 일치하지 않습니다. 다시 입력해주세요
패스워드를 입력하세요 (영문 숫자 포함 8자 이상) :

제대로 입력시

회원가입 완료!!
'''

'''
[로그인]
아이디를 입력하세요 : 
 > 틀리면 아이디가 일치하지 않습니다.
 
패스워드를 입력하세요 : 
 > 틀리면 패스워드가 일치하지 않습니다.
 
둘다 일치한다면
로그인 성공!!
환영합니다.
'''

print('[회원가입]')

# ID입력, 오류 발생시 안내문구
id_input = input('아이디를 입력하세요(3글자 이상) : ')
while True :
    if len(id_input) < 3 :
        print('입력오류 : 3글자 이상을 입력하세요')
        id_input = input('아이디를 입력하세요(3글자 이상) : ')
    else :
        break

# PW입력, 오류 발생시 안내문구
pw_input = input('패스워드를 입력하세요(영문,숫자 혼합 8자 이상) : ')
while True :
    if len(pw_input) < 8 : # 8글자 미만인 경우 오류
        print('입력오류 : 8글자 이상을 입력하세요')
        pw_input = input('패스워드를 입력하세요(영문,숫자 혼합 8자 이상) : ')

    elif pw_input.isalpha() == True or pw_input.isnumeric() == True : # 문자, 숫자 혼합이 아닌 경우 오류
        print('입력오류 : 영문, 숫자를 혼합하세요')
        pw_input = input('패스워드를 입력하세요(영문,숫자 혼합 8자 이상) : ')
    else :
        break

# 패스워드 확인하기

print('패스워드 확인')
re_pw_input = input('패스워드를 다시 입력하세요 : ')

while True :
    if pw_input != re_pw_input :
       print('패스워드가 일치하지 않습니다.')
       re_pw_input = input('패스워드를 다시 입력하세요 : ')

    else :
        print('회원가입 완료!!')
        break



print('[로그인]')

id_login = input('아이디를 입력하세요 : ')
while True :
    if id_input != id_login :
       print('아이디가 일치하지 않습니다.')
       id_login = input('아이디를 입력하세요 : ')
    else :
        break

pw_login = input('패스워드를 입력하세요 : ')
while True :
    if pw_input != pw_login :
       print('패스워드가 일치하지 않습니다.')
       pw_login = input('패스워드를 입력하세요 : ')
    else :
        print('로그인 성공! 환영합니다!')
        break