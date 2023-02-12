

class Car :

    max_oil = 50 # 최대 주유량, class 변수로 Car class로 만든 모든 객체가 공유하는 숫자

    def __init__(self, oil):
        self.oil = oil

    def add_oil(self, charge_oil):
        if charge_oil <= 0: # 0이하의 주유는 진행하지 않음
            return

        self.oil += charge_oil

        if self.oil > Car.max_oil : # 주유 후 최대 주유량 초과 상태이면
           self.oil = Car.max_oil

    def car_info(self):
        print('현재 주유상태 : {}'.format(self.oil))

class Hybirid(Car):

    max_battery = 30 #최대 충전량, class 변수 Hybrid class의 모든 객체가 공유하는 변수
    def __init__(self, oil, battery):
        super().__init__(oil) # 엄마의 __init__ 다 가져옴
        self.battery = battery

    def charge(self, charge_battery):
        if charge_battery <= 0 :
            return
        self.battery += charge_battery
        if self.battery > Hybirid.max_battery :
            self.battery = Hybirid.max_battery

    def hybrid_info(self):
        super().car_info()
        print('현재 충전상태 : {}'.format(self.battery))

car = Hybirid(0,0)
car.add_oil(100)
car.charge(50)
car.hybrid_info()