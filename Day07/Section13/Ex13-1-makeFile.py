'''

파일 입출력 (I/O - input/output)
    입력(input) 기존 파일 읽어들이는 것
    출력(output) 파일 생성, 내용 추가를 말한다.
'''

file = open('myfile.txt', 'wt')  # open 메소드 이용, 같은 폴더내 파일 생성
print('myfile.txt 파일이 생성되었습니다.')
file.close()

# with문 - 자동으로 close() 해준다.
with open('myfile.txt','wt') as file:
    print('myfile.txt 파일이 생성되었습니다.')