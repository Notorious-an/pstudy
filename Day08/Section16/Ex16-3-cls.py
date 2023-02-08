'''

클래스 변수
    클래스를 기반으로 만든 모든 인스턴트가 공유할 수 있는 변수
    클래스 정의문 바로 아래 대입된 변수
    클래스 객체로부터 참고 가능
    인스턴트  객채로부터 참고 가능
    변경 - 모든 인스턴트가 변경

인스턴트 변수
    그 인스턴트만 사용 하는 값
    함수 정의문 바로 아래 대입된 self의 속성변수
    클래스 객체로부터 참고 불가능
    인스턴트 객체로부터 참고 가능
    변경 - 그 인스턴트의 속성만 변경

클래스 메소드
    인스턴트가 없어도 클래스를 이용해 호출할 수 있으며
    cls 이용해 클래스 변수를 사용 할 수 있다.
'''

class Bag:
    count = 0 # 클래스 변수, 이건 객체를 만들어도 객체들이 공유하는 값, 각 인스턴트 들이 변경가능

    def __init__(self):
        Bag.count += 1   # init에 있기 떄문에 객체를 만들떄 마다 +1이 되어서 count 값이 올라감

    @classmethod
    def sell(cls):
        cls.count -= 1

    @classmethod
    def remain_bag(cls):
        return cls.count  #class 변수니까 self 대신에 cls사용

    @staticmethod
    def slogan(): # 일반 메소드와 동일한데, cls값 없이 바로 쓸수 있다.
        print('명품 주인을 찾습니다.')

print('현재 가방 : {}개'.format(Bag.remain_bag())) # class 메소드라 객체 안만들어도 사용가능

Bag.slogan()

bag1 = Bag() # 객체 생성
bag2 = Bag() # 객체 생성
bag3 = Bag() # 객체 생성


# init이 3번이 생성되어서 class 변수에 영향을 줘서 3개가 됨
print('현재 가방 : {}개'.format(Bag.remain_bag()))