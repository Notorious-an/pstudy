'''

CSV(comma-separated values)
    필드를 쉼표(,)로 구분한 텍스트 파일을 의미함

인공지능 분야가 발달하면서, 엑셀파일로 호환이 좋은 파일이 CSV 파일이라서 많이 쓰임
'''

student_list = []
with open('학생명단.csv', 'rt', encoding = 'UTF-8') as file :
    file.readline()
    while True :
        line = file.readline() # readline()은 str으로 인식함
        if not line :
            break
        student = line.split(',')
        student_list.append(student)
print(student_list)