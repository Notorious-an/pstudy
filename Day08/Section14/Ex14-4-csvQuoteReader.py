member_list = []
with open('회원명단.csv', 'rt', encoding='UTF-8') as file:
    file.readline() # 첫줄 제목줄 제거
    while True:
        line = file.readline() # 두번쨰줄 부터 읽기
        if not line:
            break
        member = line.split(',')
        member[0] = member[0].strip('"')  # 쌍따옴표 제거하기
        member[2] = member[2].strip('\n') # 개행 제거하기
        # 눈에는 안보이지만 마지막 다음엔 개행이 있음

        member_list.append(member)

print(member_list)
