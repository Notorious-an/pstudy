'''
파일명 : Ex01-Linear.py

자료구조(DataStructure)
    자료구조는 컴퓨터 과학에서 효율적인 접근 및 수정을 가능케 하는
    자료의 조직, 관리, 저장을 의미한다.

선형 리스트(Linear List)
    데이터를 일정한 순서로 나열한 구조
    순차 리스트(Ordered List)라고도 한다.
    입력 순서대로 저장하는 데이터에 해당한다.
    선형 리스트는 메모리에서도 차례로 저장된다.

    삽입
        1단계 : 맨끝에 빈칸을 확보한다.
        2단계 : 삽입하고자 하는 공간에 빈칸이 없으므로, 사입하고자 하는 공간 뒤에 있는
            요소들을 한칸씩 뒤로 옮긴다.
        3단계 : 빈자리에 요소를 삽입한다.

    삭제
        원하는 요소가 삭제된 후 빈칸을 그대로 두지 않고 뒤의 요소들을 앞으로 한칸씩 이동시킨다.

'''
class LinearList():
    def __init__(self):
        self.linear = []

    def add_data(self, data):
        linear = self.linear
        linear.append(None)
        lLen = len(linear)
        linear[lLen - 1] = data

    def insert_data(self, position, data):
        linear = self.linear

        if position < 0 or position > len(linear):
            print('데이터 범위를 벗어났습니다.') # 유효성 검사

        linear.append(None) # 마지막 빈칸 하나 추가하기

        # position 뒷자리 부터 한칸씩 뒤로 밀기
        lLen = len(linear)
        for i in range(lLen - 1, position, -1):
            linear[i] = linear[i-1]  # 하나씩 데이터 밀어주고
            linear[i-1] = None # 그자리는 none 값이 들어간다
        # 포지션 자리에 data 입력
        linear[position] = data


    def delete_data(self, position):
        linear = self.linear
        lLen = len(linear)

        if position < 0 or position > len(linear):
            print('데이터 범위를 벗어났습니다.') # 유효성 검사



        for i in range(lLen - 1, position, -1):
            linear[i-1] = linear[i]  # 하나씩 데이터 당겨준다
            linear[i] = None
        linear.pop()



    def print_list(self):
        linear = self.linear
        for list in linear:
            print(list)

# 실행코드
linear = LinearList()
linear.add_data(3)
linear.add_data(5)
linear.add_data(4)
linear.add_data(2)
linear.add_data(6)

linear.delete_data(3)

linear.print_list()

