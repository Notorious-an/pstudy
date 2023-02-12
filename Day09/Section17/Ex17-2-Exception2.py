
'''

예외(Exception)
    프로그램 존재하는 오류 비슷하지만
    개발자가 직접 처리할 수 있는 간단한 문제를 예외라고 한다.
'''

try:
    a = int(input('제수를 입력하세요 : '))
    b = int(input('피제수를 입력하세요 : '))
    print('{} / {} = {}'.format(a, b, a / b))

except: # 오류 발생시
    print('예외가 발생했씁니다.')

