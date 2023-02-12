
class HourError(Exception): # Exception 자체가 클래스라서 상속받을 수 있다.

    def __init__(self):
        super().__init__('올바른 시간이 아닙니다.')  # HourError() 기본값이 '올바른 시간이 아닙니다'

try:
    hour = int(input('시간을 입력하세요:'))
    if hour < 0 or hour > 23:
        raise HourError

except HourError as e:
    print(e)