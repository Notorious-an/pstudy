'''
Set에 대해 배워보자
    순서가 없다
    인덱싱되지 않는 collection
    중복값이 없다(중요, set 쓰는 이유)
'''

# 순서가 없다. 실행할 때 마다 순서가 변경
set1 = {'apple', 'banana', 'cake', 'donut', 'egg', 'fruit', 'grape', 'hotdog'}
print(set1)

# 순서 없이 가져옴
for x in set1 :
    print(x)

# 값이 있는지 확인하기
print("carrot" in set1)  # False 값 출력된다.
print("apple" in set1)  # True 값 출력된다.

# set 항목 추가하기 : add 메소드 사용한다
set1.add("icecream")
print(set1)

# 다른 Set 항목 추가하기 : update 메소드 사용한다
set2 = {"juice", "kakao"}
set1.update(set2)
print(set1)

# 항목 제거하기 : remove 메소드 / discard 메소드 / pop 메소드
set1.remove("apple") # 없는 항목 제거시 에러
print(set1)
set1.discard("banana") # 없는 항목 제거시 에러x
print(set1)
set1.pop() # 랜덤으로 하나씩 제거 한다
print(set1)

# set 비우기
set1.clear()
print(set1)