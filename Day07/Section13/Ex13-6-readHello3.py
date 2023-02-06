'''
파일명 : Ex13-6-readHello3.py

readline()
    파일에서 1줄을 읽고 그 결과를 리턴
'''
with open('hello.txt', 'rt', encoding='UTF-8') as file:
    while True:
        str = file.readline()  # 위에줄 부터 한줄씩 읽어오기

        if str == '':
            break
        print(str, end='')
