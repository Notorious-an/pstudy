'''
리스트에 대해서 학습해보자, 변화할 수 있는 변수 모음집
'''

thisislist = [1,2,3,"피카츄"]
list1 = [True,False,True,False]
list2 = [2,3,4,5]
list3 = ["abc",34,False,40]
list4 = ["피카츄","잠만보","나옹이","또가스"]

# 리스트 길이 구하기
print(len(list1)) # 정답은 4

# 리스트 인덱싱, 슬라이싱
print(list2[2:3])

# 변경  // 2개 항목 변경
list3[0] = "def"  # ["def",34,False,40]
print(list3)

list4[1:3] = ["울먹이","야도란"]
print(list4)

list4[1:3] = ["울먹이"]
print(list4)

# 항목 추가하기 * append 메소드 사용, 마지막 항목에 추가하는 것
list4.append("꼬부기")
print(list4)

# 항목 추가하기 * 인덱스 번호 사용, 원하는 위치에 추가
list4.insert(1,"잠만보")
print(list4)

# 항목 값으로 제거하기
list4.remove("잠만보")
print(list4)

# 항목 지정된 인덱스로 제거
list4.pop(2)  # 참고로 list4.pop()은 마지막 값이 삭제된다
print(list4)

# 목록 전부 삭제하기
list4.clear()
print(list4)

# 확장하기
list4.extend(["버터플", "야도란"])
print(list4)

# 완전 삭제해버리기
del list4  # 리스트 자체를 통째로 날려버리기