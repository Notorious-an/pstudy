dan = 2
while dan <= 9 :
    n = 1
    while n <= 9 :
        print('{}x{}={}'.format(dan, n, dan*n), end = ' ')
        n = n + 1
    dan = dan + 1
    print() # 행을 다음줄에 쓰는 코드