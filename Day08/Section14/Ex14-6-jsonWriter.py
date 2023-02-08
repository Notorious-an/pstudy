'''
JSON(JavaScript Object Notation)
 - 딕셔너리 비슷하다     딕셔너리(파이썬) <-> json 을 배워보자
 - 구조 {key : value}
 - 파이썬 dictionary 자료 구조 -> json 파일 바꾸는 메소드 json.dumps(객체)
'''

import json

# 첫번째 방법

'''
dict_list = [
    {
      'name':'james',
      'age':20,
      'spec':[175.5, 70.5

              ]

    },
    {
        'name':'alice',
        'age':21,
        'spec':[
            168.5,
            60.5

        ]
    }

]

# (mothod 설명) json.dumps(dictionary) dictionary 자료구조를 json 파일로 바꿔주는 메소드
# json type 파일을 open(만들어서) 후 json 파일을 쓴다.

json_string = json.dumps(dict_list)

with open('dictList.json', 'w') as file:
    file.write(json_string)
print('dictList.json 파일이 생성되었습니다.')

'''

# 두번째 방법

dict_list = [
    {
      'name':'홍길동',
      'age':20,
      'spec':[175.5, 70.5

              ]

    },
    {
        'name':'어우동',
        'age':21,
        'spec':[
            168.5,
            60.5

        ]
    }

]

json_string = json.dumps(dict_list, indent=4, ensure_ascii=False)
# 이 과정에서 한글이 안깨지게 하기 위해서 ensure 옵션
# 한줄이 아닌 들여쓰기를 하는 것은 indent 옵션

with open('dictList.json1', 'w', encoding='UTF-8') as file:
    file.write(json_string)
print('dictlist1.json 파일이 생성되었습니다.')