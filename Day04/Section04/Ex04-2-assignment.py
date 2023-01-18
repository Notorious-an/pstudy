'''
대입 연산자
    변수에 값을 저장하기 위해 사용하는 대입 연산자
print 형식문자
%d = 숫자 데이터
%f = 실수 데이터
%o = 8진수 데이터
%s = 문자열 데이터
%c = 문자 하나 데이터
'''

a, b = 10, 20
print('a = %d, b = %d' %(a, b))
a, b = b, a
print('a = %d, b = %d' %(a, b))

'''
복합 대입 연산자
+=  ex x += 3 과 x = x+3 과 같다
-=  ex x -= 3 과 x = x-3 과 같다
'''

piggy_bank = 0
money = 10000
piggy_bank += money
print('저금통에 용돈 {}원을 넣었습니다'.format(money))
print('지금 저금통에는 {}원이 있습니다'.format(piggy_bank))

snack = 2000
piggy_bank -= snack
print('저금통에서 스낵구입비 {}원을 뺐습니다.'.format(snack))
print('지금 저금통에는 {}원이 있습니다..'.format(piggy_bank))


