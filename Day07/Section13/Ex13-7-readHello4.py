'''
한줄씩 다 읽어와서 리스트로 반환
'''
with open('hello.txt', 'rt') as file :
    line_list = file.readlines()
    print(line_list)
    for line in line_list :
        print(line, end='')