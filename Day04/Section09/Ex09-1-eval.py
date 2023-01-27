'''
내장함수 알아보기
eval() 함수
    매개변수로 받은 expression(=식)을
    문자열로 받아서 계산해주는 함수
'''

exp = input('계산식을 입력하세요 :')
result = eval(exp)  # 문자열을 계산해주는 함수
print(exp + '=' + str(result))

