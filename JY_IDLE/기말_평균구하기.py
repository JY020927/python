#학생 수와 과목 수를 입력받은 후, 학생의 평균을 구하는 프로그램을 작성하시오.(이중 for문 이용)

num=int(input("전체 학생수는 : "))
course=int(input("과목수 : "))

for i in range(num):
    sum = 0
    for j in range(course):
        point = int(input("%d번 학생의 과목%d 점수 : " % (i+1, j+1)))
        sum += point
    print("%d번 학생의 성적 평균 : %.1f" % (i+1, sum/course))
