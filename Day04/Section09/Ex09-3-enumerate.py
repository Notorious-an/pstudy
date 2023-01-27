'''
enumerate()
    List, Tuple, String 등 자료형을 입력받으면
    인덱스 값을 포함하는 enumerate 객체를 돌려준다.
'''
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

print(len(month))  # list값을 개수는?
for m, day in enumerate(month) :  # 인덱스 값, 리스트 값을 돌려준다
    print('{}월의 일수는 {}일 입니다.'.format(m+1, day))
