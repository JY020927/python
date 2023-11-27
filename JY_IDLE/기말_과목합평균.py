#과목수를 입력받아 과목의 합과 평균을 구하시오. (for 이용)
course = int(input("과목수 : "))
sum = 0

for i in range(course):
    point = int(input("과목%d 점수 : " % (i+1)))
    sum += point

print("과목합 : %d, 성적 평균 : %.1f" % (sum, sum/course))
