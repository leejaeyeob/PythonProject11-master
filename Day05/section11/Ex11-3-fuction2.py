def get_average(total):
    total = 0
    for subjact in marks:
        total += marks[subjact]

    l_average = total / len(marks)
    return l_average

marks = {'국어': 90, '영어': 80, '수학': 85}
average = get_average(marks)
print('평균은 {}점 입니다.'.format(average))
