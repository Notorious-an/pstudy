'''
클래스 상속 개념 잡기 예제
'''

class A:
    def greeting(self):
        print('안녕하세요. A입니다.')

class B(A):
    def greeting(self): # 상속 받았지만 greeting 함수 재정의 함(오버라이딩이라고 함)
        print('안녕하세요, B입니다.')

class C(B):
    def greeting(self):
        print('안녕하세요. C입니다')

class D(C,B):
    pass # 내부동작 필요없고 빈껍데기만 필요할때 pass 사용 (단순히, B+C인 클래스 만듬)

x = D()
x.greeting()

