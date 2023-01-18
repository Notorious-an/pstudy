'''
튜플에 대해서 알아봅시다
    단일 변수에 여러 항목을 저장하는데 사용된다.
    순서가 있고, 변경 할 수 없는 List
    둥근 괄호로 작성됩니다. Ok? Are you understand?
'''

tuple1 = ("피카츄","파이리","꼬부기")
print(tuple1)

# 튜플의 길이
print(len(tuple1)) # 정답은 3

# 항목 접근 : 인덱싱, 슬라이싱
print(tuple1[0], tuple1[-1], tuple1[0:2])

# 튜플값 변경 방법 : 리스트로 바꾸어서 변경해줘야 함, 정말 억지스럽네
list1 = list(tuple1) # 리스트로 바꾼다
list1[0] = "잠만보"  # 리스트에서 항목 변경
tuple1 = tuple(list1) # 리스트를 다시 튜플로 변경
print(tuple1) # 튜플 출력한다

# 튜플 압축풀기
tuple2 = ("apple", "banana", "cake", "donut")
(p1, p2, p3, p4) = ("apple", "banana", "cake", "donut") # 각 값에 튜플 하나씩 대응
print(p1)
print(p2)
print(p3)
print(p4)

# 두개의 튜플 조인
tuple3 = ("apple", "banana", "cake", "donut")
tuple4 = ("egg", "fruit", "grape", "ham")
tuple5 = tuple3 + tuple4
print(tuple5)

