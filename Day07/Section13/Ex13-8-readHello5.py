
with open('hello.txt', 'rt') as file :
    line_list = file.readlines()
    for no, line in enumerate(line_list):
        print('{} {}'. format(no+1, line))
