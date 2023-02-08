
# 만들어낸 객체들이 변경가능하거나 공유할 내용은 class 변수, class 메소드로 기입해줘야 한다.

# 이번 예제에서 player1 이라는 인스턴트 객체들은 card3~card7 정보를 공유하고,
# class 메소드는 굳이 객체 생성을 안하고 class명.메소드 명으로 바로 사용할 수 있다.

class HoldemPlayer:
    card3 = ''  # 클래스 변수, 모든 객체가 공유가능하고 변경가능한 변수
    card4 = ''
    card5 = ''
    card6 = ''
    card7 = ''

    def __init__(self, card1, card2):
        #  객체를 생성할 때 반드시 호출이 되고
        #  제일 먼저 실행되는 일종의 메서드라고 생각하면 편하다.
        self.card1 = card1
        self.card2 = card2

    def get_card_info(self):
        print('card1:{}'.format(self.card1))
        print('card2:{}'.format(self.card2))
        print('card3:{}'.format(self.card3))
        print('card4:{}'.format(self.card4))
        print('card5:{}'.format(self.card5))
        print('card6:{}'.format(self.card6))
        print('card7:{}'.format(self.card7))

    @classmethod
    def set_card3(cls, card):
        cls.card3 = card

    @classmethod
    def set_card4(cls, card):
        cls.card4 = card

    @classmethod
    def set_card5(cls, card):
        cls.card5 = card

    @classmethod
    def set_card6(cls, card):
        cls.card6 = card

    @classmethod
    def set_card7(cls, card):
        cls.card7 = card


player1 = HoldemPlayer('SpadeA', 'SpadeK')
player2 = HoldemPlayer('Dia2', 'Dia7')
player1 = HoldemPlayer('Heart10', 'HeartK')


print('1round Player의 카드정보 입니다.')
player1.get_card_info()
print('>>>>>>>>>>>>>>>>>')
player2.get_card_info()

print('2round Player의 카드정보 입니다.')
HoldemPlayer.set_card3('Heart2')
player1.get_card_info()
print('>>>>>>>>>>>>>>>>>')
player2.get_card_info()
