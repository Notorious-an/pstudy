'''
클래스 상속
    어떤 클래스가 가지고 있는 기능을
    그대로 물려받아 사용할 수 있는 클래스

상속 방법
class 슈퍼클래스
    본문
class 서브클래스(슈퍼클래스)
    본문

모듈과 클래스의 차이점 : 클래스는 상속이 가능하다.
'''

class coffee:

    def __init__(self, bean):
        self.bean = bean

    def coffee_info(self):
        print('원두:{}'.format(self.bean))

# 서브 클래스(자식 클래스)
class Espresso(coffee):
    # 상속 선언을 하면서 부모가 가지고 있는 변수, 메소드를 그대로 가지고 오면서 조금 추가하거나 수정할떄
    def __init__(self, bean, water):
        super().__init__(bean)  # coffee 클래스의 생성자 가져오기
        self.water = water
    def espresso_info(self):
        super().coffee_info() # coffee 클래스의 메소드 가져오기
        print('물:{}ml'.format(self.water))

coffee1 = Espresso('콜롬비아',30)
coffee1.espresso_info()