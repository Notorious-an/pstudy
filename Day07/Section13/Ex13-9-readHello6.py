
import sys

with open('hello.txt', 'rt') as file :
   line_list = file.readlines()
   sys.stdout.writelines(line_list)

# sys _ os라는 뜻, os에 대한 정보를 담고 있는 객체라고 보면 됨
# sys에서 standard out 하란 뜻 = 즉 print 하라는 뜻.