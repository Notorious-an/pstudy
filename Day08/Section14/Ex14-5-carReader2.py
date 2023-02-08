'''
csv 모듈 사용하기
'''
import csv

with open('차량관리1.csv', 'r', encoding='UTF-8') as file:
    car_reader = csv.reader(file, delimiter =',', quotechar = '"')

    # csv 모듈을 사용하기 때문에 csv.reader 쓴다.
    # (중요) csv.read() 함수는 반복가능한 iterator 객체를 반환하므로,
    # 그 자체는 출력값이 없으며 for문을 통해 한 라인씩 가져 올 수 있다.

    for line in car_reader :
        print(line)