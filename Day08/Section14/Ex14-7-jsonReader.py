''
json.load()는 json 형태를 파이썬 딕셔너리로 바꿔주는 메소드
'''


import json
with open('dictList.json', 'r', encoding='UTF-8') as file : # 읽기모드로 json파일 열기
    json_reader = file.read() # json파일 읽어오기
    
    dict_list = json.loads(json_reader)  # json.load()는 json 형태를 파이썬 딕셔너리로 바꿔주는 메소드

for dic in dict_list :
    print('이름 : {}'.format(dic['name']))
    print('나이 : {}'.format(dic['age']))
    print('키 : {}'.format(dic['spec'][0]))
    print('몸무게 : {}'.format(dic['spec'][1]))
    print()
