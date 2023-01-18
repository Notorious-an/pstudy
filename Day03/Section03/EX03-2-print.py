'''
print() 함수 사용법
    sep : 출력할 value의 구분 문자
    end : value 출력 후 출력할 문자(기본값 '\n') -> 즉 기본 값이 다음행에 출력한다는 뜻
    file : 출력 방향 지정
'''

print('재미있는','파이썬')
print('Python','Java','C', sep=',')
print('Python','Java','C', sep='|')
print('Python','Java','C', sep=' ')
print("안녕", end = '')
print("하세요")

# 매크로 할 때 이런식으로 한다
fos = open('sample.py', mode='wt')  #wt 는 write text 라는 뜻
print('print("Hello World")', file=fos)  #file에다가 쓴다는 뜻 #최종 목적지
fos.close()

