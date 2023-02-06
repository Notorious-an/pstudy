'''
파일 복사하기
    원본 -> 버퍼 변수 (Memory) -> 복사본
    rb : read binary 모드   # text가 아닌 컴퓨터가 가진 binary 값 복사
'''

buffer_size  = 1024 # 1024byte -> 1KB 의미
with open('hello.txt', 'rb') as source:
    with open('hello2.txt', 'wb') as copy: # open 함수는 파일 없으면 hello2 만든다.
        while True :
            buffer = source.read(buffer_size) #매개변수로 size를 넣어줌
            if not buffer:
                break
            copy.write(buffer)
print('hello2.txt 파일이 복사되었습니다.')