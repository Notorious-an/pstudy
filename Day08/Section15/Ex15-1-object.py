'''

클래스
    객체를 만드는 설계도
    붕어빵 틀, 와플 긱/ㅖ
    객체화(인스턴트화) - 메모리에 올리는 것


객체(object)
    현실 세계에 존재하는 물리적, 추상적 식별할 수 있는 모든 것을 말함
    ex) 컴퓨터, 학생, 주문, 배송

객체 구성
    초기화용 - 생성자
    속성 값 - 변수
    기능 - 메소드(함수)


클래스를 쓰는 이유는 여러가지 메소드를 class라는 이름으로 묶어준다고 보면됨
ex) str.replace  str이라는 클래스 밑에 여러가지 메소드가 있다....
그룹화를 통해서 메소드(함수)를 개념적으로, 기능적으로 묶어 놓은 것!!
'''

# 예제) computer 클래스 정의

class Computer : # 붕어빵 기계 만들기
    def set_spec(self, cpu, ram, vga, ssd):  # 메소드 1, 변수 4개
        self.cpu = cpu  # 매개 변수 cpu를 나 자신에게 받아오도록 정의해줌
        self.ram = ram
        self.vga = vga
        self.ssd = ssd
    # 참고로 self는 class 나 자신을 의미함, 클래스 만들때만 사용된다.
    def hardware_info(self): # 메소드 2, 변수 없음
        print('CPU = {}'.format(self.cpu))
        print('RAM = {}'.format(self.ram))
        print('VGA = {}'.format(self.vga))
        print('SSD = {}'.format(self.ssd))

desktop = Computer() # 붕어빵 틀인 클래스로, desktop이라는 붕어빵 만듦
# Class에 있는 메소드 사용하려면 클래스로 객체를 만들어 줘야 함!!!!
# 이제 desktop은 Computer class에 있는 메소드 사용 가능하다

desktop.set_spec('i7', '16GB', 'GTX3060', '23434') # 변수 4개 필요함
desktop.hardware_info() # 변수 필요 없음


