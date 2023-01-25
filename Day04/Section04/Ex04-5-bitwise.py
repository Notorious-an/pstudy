'''
비트 연산자 (중요도는 떨어지는데 난이도는 상)

    어떤 변수의 값을 0과 1의 조합인 2진수
    &(and) 입력이 모두 1이면 1, 아니면 0
    |(or) : 입력 중 하나라도 1이면 1, 아니면 0
    ^(XOR) : 입력이 서로 다르면 1, 아니면 0
    ~(NOT) : 입력이 0이면 1, 입력이 1이면 0
    <<(왼쪽 SHIFT) : 비트 단위로 왼쪽으로 N비트 이동하며 2의 N 거듭제곱만큼 곱셈
    >>(오른쪽 SHIFT) : 비트 단위로 오른쪽으로 N비트 이동하며 2의 N 거듭제곱만큼 나눗셈
'''

a = 6  # 2진수 0110
b = 5  # 2진수 0101

print('a & b : {}'.format(a & b))  # 답 4
 # 0110
 # 0101
 # 0100 -> 값 4!!

print('a | b : {}'.format(a | b)) # 답 7
 # 0110
 # 0101
 # 0111 -> 값 7!!

print('a ^ b : {}'.format(a ^ b)) # 답 3

 # 0110
 # 0101
 # 0011 -> 값 3!!  서로 달라야 True(1) "exclusive or" 이라고 부른다

print('a << 1 : {}'.format(a << 1)) # 답 12
 # 0110 # 왼쪽으로 한칸씩 이동시켜라
 # 1100 -> 값 12!!

print('a >> 1 : {}'.format(a >> 1)) # 답 3
 # 0110 # 오른쪽으로 한칸씩 이동시켜라
 # 0011 -> 값 3!!

print('~a : {}'.format(~a)) # 답 -7
 # 0(부호비트, 숨어있다)  0110       # 입력이 0이면 1, 입력이 1이면 0, 부호 비트도 바꿔줘야 한다
 # 1(부호비트, 숨어있다)  1001       # ??

