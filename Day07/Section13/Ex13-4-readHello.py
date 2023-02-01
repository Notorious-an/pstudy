'''

파일 읽기모드

r(read me) : 읽기 전용 모드 / 파일 없으면 에러

경로
    절대경로 예) C:\pstudy\Day07\Section13\hello.txt
               =  C://pstudy//Day07//Section13//hello.txt
    상대경로
        예) ./upload/hello2.txt
            ../../resources/hello.txt
        . -> 현재폴더
        .. -> 상위 폴더

'''


file = open('../hello3.txt', 'rt') # 읽기 모드로 열어서 파일을 읽어오라
  # 여기서 hello.txt 대신에 절대경로를 써도 된다.

str = file.read()
print(str, end='')
file.close()


with open('hello.txt', 'rt') as file :  # with문으로 사용하기
    str = file.read()
    print(str, end='')