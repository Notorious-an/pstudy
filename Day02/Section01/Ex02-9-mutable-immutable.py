'''
Mutable - 메모리 값을 변경 가능 객체
ㅡ   리스트(list), 세트(set), 딕셔너리(dict)

'''

me = [1,2,3,]
print(id(me)) # 주소값 : 1383660379520
me.append(4)
print(id(me)) # 주소값 : 1383660379520


'''
immutable - 메모리 값 변경 불가
    정수(int), 실수(float), 문자열(str), 튜플(tuple)
'''

me = 10
print(id(me)) # 주소값 : 140732571266240
me += 1 # me = me + 1
print(id(me)) # 주소값 : 140732571266272