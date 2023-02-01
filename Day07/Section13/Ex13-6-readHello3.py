'''
readline 한줄씩 읽어오기
'''
with open('hello.txt', 'rt') as file :
    while True :
        str = file.readline()
        if not str :
            break

        print(str)