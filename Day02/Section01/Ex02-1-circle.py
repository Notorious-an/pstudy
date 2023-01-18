
# 큰 따옴표("""세개""")는 docstring 코드의 문서화에 도움이 되는 문자열을 말한다

# matn 모듈 포함
import math
#get_area() 함수 정의

def get_area(radius):
    """반지름을 전달하면 원의 넓이를 반환하는 get_area() 함수"""
    area = math.pi * math.pow(radius, 2) # math 모듈에 있는 pow 라는 함수(제곱함수)
    return area

radius = 1.5
print(radius)

# get_area() 함수 호출 결과를 area 변수에 저장
area = get_area(radius)
print(area)
print(get_area.__doc__) # get_area안에 있는 docstring 확인
