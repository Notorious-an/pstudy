'''
생성자
    인스턴트를 생성할 떄 생성자가 자동으로 호출된다.
    객체 초기화 용으로 사용한다.

    생성자는 new 연산자를 통해 객체를 생성할 때 반드시 호출이 되고
    제일 먼저 실행되는 일종의 메서드라고 생각하면 편하다.
    (메서드와 비슷하지 그 의미가 같은 것은 아니다) 생성자는 멤버 변수를 초기화하는 역할을 한다.
'''

class USB:
    # 생성자
    def __init__(self,capacity):
        self.capacity = capacity
    def info(self):
        print('{}GB USB'.format(self.capacity))

usb = USB(1230)
usb.info()