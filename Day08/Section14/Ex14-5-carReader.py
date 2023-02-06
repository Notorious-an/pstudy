'''
csv 모듈 사용하기
'''
import csv

with open('차량관리1.csv', 'r', newline='', encoding='UTF-8') as file:
    # newline 기본값이 개행되는 것이기 떄문에
    # newline=''을 지정하지 않으면,
    # 따옴표 처리된 필드에 포함된 줄 넘김 문자가 올바르게 해석되지 않으며,
    # 줄 끝 표시에 \r\n을 사용하는 플랫폼에서 쓸 때 여분의 \r이 추가됩니다.
    # csv 모듈은 자체 (유니버설) 줄 넘김 처리를 하므로,
    # newline=''을 지정하는 것은 항상 안전합니다.

    car_reader = csv.reader(file, delimiter =',', quotechar = '"') # csv 파일 한줄씩 읽기
    # text 파일이 아니기 떄문에 readline()이 아니라 csv.reader 쓴다.
    for line in car_reader :
        print(line)