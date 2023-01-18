'''

Dictionary
    Key:value로 이루어져 쌍으로 데이터 값을 저장하는데 사용

'''

# dictionary 선언
dict1 = {"brand":"나이키","model":"max90","year":1990}
print(dict1)

'''
키 이름을 사용하여 참조할 수 있다.
'''
#값 가져오기 - key 값으로,value 값을 찾아올 수 있다
dict1 = {"brand":"나이키","model":"max90","year":1990}
## 형식 1 - dict1[key] = value
## 형식 2 - dict1.get(key) = value
print(dict1["brand"])
print(dict1.get("model"))

# 키 목록 가져오기
print(dict1.keys())

# 추가하기
dict2 = {"brand":"Ford","model":"Mustang","year":1964}
dict2["color"] = "red" # 방법 1
print(dict2)
dict2.update({"bgColor":"Black"})
print(dict2)

# 변경하기
dict2["brand"] = "Toyota"
dict2.update({"model":"Siena"})
print(dict2)

# 제거하기
dict2.pop("bgColor")
print(dict2)