'''
for문, while 문과 같은 반복문을 강제로 건너뛰기
(아래 코드를 실행하지 않는다, 반복문으로 돌아가라)
'''

total = 0
for a in range(1, 101) :
    if a % 3 == 0 : # a가 3의 배수일때
        continue # 아래 코드 실행안하고 다시 for 문으로 돌아가라, 3의 배수는 건너뛰기
    print('a: {}, total : {}'.format(a, total))
    total = total + a
print(total)

# continue 문을 활용해서 3의 배수는 건너뛰었다.