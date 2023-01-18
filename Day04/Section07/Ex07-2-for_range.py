dan = int(input('출력할 구구단을 입력하세요 : '))

for n in range(10) : # range(10) : 0~9라는 뜻
    print('{}x{}={}'.format(dan,n, dan*n), end = ' ')
print()


for n in range(1,10) : # range(10) : 1~9라는 뜻
    print('{}x{}={}'.format(dan,n, dan*n), end = ' ')
print()

for n in range(1,10, 2) : # range(10) : 1~9 중에 2개씩 건너뛰기
    print('{}x{}={}'.format(dan,n, dan*n), end = ' ')
print()