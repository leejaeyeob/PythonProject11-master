'''
데이터 시각화(data visualization)
    데이터를 분석한 결과를 사용자가 쉽게 이해할 수 있도록
    표현하여 전달한 것을 의미한다.

    1. 많은 양의 데이터를 한 눈에 살펴볼 수 있다.
    2. 전문지식이 없더라도 누구나 쉽게 해당 데이터 인지 사용할 수 있다.
    3. 단순한 데이터의 요약이나 나열보다 더 정확한 데이터 분석 결과를 얻을 수 있다.
    4. 단순한 데이터에서 알 수 없었던 중요한 정보를 파악할 수 있다.
'''

import matplotlib.pyplot as plt
figure = plt.figure()
axes = figure.add_subplot(111)  # 행, 열, 번호
x = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
y = [1280, 800, 500, 400, 700, 800]
axes.plot(x, y, linestyle='--', marker='^', color='red')
plt.show()
