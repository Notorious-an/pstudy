'''
JSON(JavaScript Object Notation)
 - 딕셔너리 비슷하다
 - 구조 {key : value}
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