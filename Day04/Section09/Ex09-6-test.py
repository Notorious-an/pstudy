
id = ''
pwd = ''
# ID 입력
while True :
    id = input('아이디를 입력하세요(3글자이상):')
    if len(id) > 2 :
        break

    print('3글자 이상을 입력해주세요')

# PW 입력
while True :
    pwd = input('패스워드를 입력하세요(영문, 숫자 포함 8자 이상):')
    isContainAlpha = False   # 나중에 True, False 여부를 판단할 변수
    isContainNumeric = False

    if len(pwd) < 8 :
        print('영문, 숫자 포함 8자 이상 입력해주세요')
        continue

    for ch in pwd :
        if ch.isalpha() :
            isContainAlpha = True  # 조건이 맞으면 True로 바꿔줌
        elif ch.isnumeric() :
            isContainNumeric = True # 조건이 맞으면 True로 바꿔줌

    # 영문 포함 유효성 검사
    if not isContainAlpha :  # isContainAlpha 값이 false 일때 실행
        print('영문, 숫자 포함 8자이상 입력해 주세요')
        continue

    if not isContainNumeric : # isContainNumeric 값이 false 일때 실행
        print('영문, 숫자 포함 8자이상 입력해 주세요')
        continue

    # isContainAlpha, isContainNumeric 값이 둘다 True로 바뀌면 넘어감


    # 패스워드 한번더 확인 유효성 검사
    pwdcheck = input('패스워드를 한번더 입력하세요 : ')
    if pwd != pwdcheck :
        print('일치하지 않습니다. 다시 입력해주세요')
        continue

    break

print('회원가입 완료')

# 로그인 아이디
while True:
    loginId = input('아이디를 입력하세요 :')
    if id == loginId:
        break
    print('패쓰워드가 일치하지 않습니다.')

print('로그인 성공!')
print('{}님 환영합니다. :)'.format(id))