'''

'''

try :
    raise Exception('예외발생') # '예외발생'가 발생함
except Exception as e:
    print('발생한 예외 메시지는 다음과 같습니다.')
    print(e)