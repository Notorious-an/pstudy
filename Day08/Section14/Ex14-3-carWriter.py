
'''
CSV 모듈을 활용해보자
'''

import csv

# 첫번째 방법
'''
with open('차량관리.csv', 'w', encoding='UTF-8') as file: # 파일을 만든다
    csv_maker = csv.writer(file, delimiter = ',') # 파일에 다가 쓴다
    csv_maker.writerow([1, '08로1244','2020-10-20, 14:00']) # 한줄씩
    csv_maker.writerow([2, '34로1264','2020-10-20, 14:10'])
    csv_maker.writerow([3, '64로1224','2020-10-20, 14:20'])
    csv_maker.writerow([4, '46로1244','2020-10-20, 14:30'])
print('차량관리.csv 파일이 생성되었습니다.')
'''

# 두번째 방법
'''
with open('차량관리1.csv', 'w', newline = '', encoding='UTF-8') as file:
    # newline의 기본값은 none (개행), newline = '' 넣어서 개행을 없애줌
    csv_maker = csv.writer(file, delimiter = ',')
    csv_maker.writerow([1, '08로1244','2020-10-20, 14:00'])
    csv_maker.writerow([2, '34로1264','2020-10-20, 14:10'])
    csv_maker.writerow([3, '64로1224','2020-10-20, 14:20'])
    csv_maker.writerow([4, '46로1244','2020-10-20, 14:30'])

'''

#마지막 방법
with open('차량관리2.csv', 'w', newline='', encoding='UTF-8') as file:
    csv_maker = csv.writer(file, delimiter = '|', quotechar=' ') # |로 구분하겠다는 뜻
    csv_maker.writerow([1, '08로1244','2020-10-20, 14:00'])
    csv_maker.writerow([2, '34로1264','2020-10-20, 14:10'])
    csv_maker.writerow([3, '64로1224','2020-10-20, 14:20'])
    csv_maker.writerow([4, '46로1244','2020-10-20, 14:30'])