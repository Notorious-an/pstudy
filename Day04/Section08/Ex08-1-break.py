'''
break 문
    while문이나 for문과 같은
    반복문을 강제로 종료하는 제어문
'''

n = 1
while True :
    print(n)
    if n == 10:
        break  # break는 가장 가까운 반복문을 종료한다!!!!
    n = n + 1