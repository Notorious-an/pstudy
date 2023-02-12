
'''

예외(Exception)
    프로그램 존재하는 오류 비슷하지만
    개발자가 직접 처리할 수 있는 간단한 문제를 예외라고 한다.

try :
    코드 작성영역
except :
    예외 발생시 처리영역
else :
    예외 발생하지 않으면 처리되는 영역
finally :
    언제나 실행되는 영역

'''

# 발생할수 있는 에러 종류
# 1. Value Error 입력값에 정수아닌 소수점 입력시
# 2. Zero DIvision 0으로 나눌떄
# 에러 종류에 따라서 세부적으로 예외처리 가능

try:
    print('서버 접속 합니다.')
    a = int(input('제수를 입력하세요 : '))
    b = int(input('피제수를 입력하세요 : '))
    result = a / b


# try 문 안에서 에러 발생하지 않을 시 except 사용

except ZeroDivisionError: # 0으로 나누는 오류 발생시
    print('0으로 나눌 수 없습니다.')

except ValueError: # 0으로 나누는 오류 발생시
    print('정수만 입력할 수 있습니다.')
except :
    print('예외가 발생했습니다.')


# try 문 안에서 에러 발생시 else 사용
else :
    print('{} / {} = {}'.format(a,b,result))

 # finally를 써줘야 메모르가 클리어 됨
finally:
    print('서버 접속 종료합니다.')