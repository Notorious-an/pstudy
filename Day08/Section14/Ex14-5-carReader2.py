'''
csv 모듈 사용하기
'''
import csv

with open('차량관리1.csv', 'r', encoding='UTF-8') as file:
    car_reader = csv.reader(file, delimiter =',', quotechar = '"') # csv 파일 한줄씩 읽기
    # csv 모듈을 사용하기 때문에 csv.reader 쓴다.
    for line in car_reader :
        print(line)