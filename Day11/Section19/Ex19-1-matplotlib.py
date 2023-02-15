'''
데이터 시각화(data visualization)란
    데이터를 분석한 결과를 사용자가 쉽게 이해할 수 있도록 표현하여 전달 한것 의미

    1. 많은 양의 데이터를 한눈에 살펴볼 수 있다.
    2. 전문지식이 없더라도 누구나 쉽게 해당 데이터 인지 및 사용 가능
    3. 단순한 데이터의 요약이나 나열보다 더 정확한 데이터 분석 결과 도출
    4. 단순한 데이터에서 알 수 없었떤 중요한 정보 파악 가능

'''

'''
matplotlib, seaborn 라이브라리 모듈 설치하기
'''

import matplotlib.pyplot as plt
figure = plt.figure()
axes = figure.add_subplot(111) # 행, 열, 번호 의미임
x = ['jan','Feb','Mar','Apr','May','Jun']
y = [1200, 700, 300, 450, 400, 500]
axes.plot(x,y,linestyle= '--', marker = '^', color = 'red')
plt.show()


# 그림을 그리는 법을 알 필요는 없다.
# seaborn이나 matplotlib 홈페이지 들어가서 코드를 가져다 쓰면 된다.


