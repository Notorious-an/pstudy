
'''
CSV 모듈을 활용해보자
'''

import csv

# CSV 파일을 쓰기 위해서는 CSV 파일을 쓰기모드로 오픈하고, csv.writer()에 파일 객체를 넣으면 된다
# CSV writer는 writerow()라는 메서드를 통해 list 데이터를 한 라인 추가하게 된다.

# 첫번째 방법
'''
with open('차량관리.csv', 'w', encoding='UTF-8') as file: # 파일을 만든다
    csv_maker = csv.writer(file, delimiter = ',') # csv.writer() 에다가 파일 넣는다.
    
    csv_maker.writerow([1, '08로1244','2020-10-20, 14:00']) # 한줄씩
    csv_maker.writerow([2, '34로1264','2020-10-20, 14:10'])
    csv_maker.writerow([3, '64로1224','2020-10-20, 14:20'])
    csv_maker.writerow([4, '46로1244','2020-10-20, 14:30'])
print('차량관리.csv 파일이 생성되었습니다.')
'''

# 두번째 방법
'''
with open('차량관리1.csv', 'w', newline = '', encoding='UTF-8') as file:
    # csv모듈에서 데이터를 쓸때 각 라인 뒤에 빈 라인이 추가되는 문제가 있는데, 이를 없애기 위해 파일을 
      open 할떄 newline=''와 같은 옵션을 지정한다. 
      
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