class St(object):
  def __init__(self, name, num, grade1, grade2, avg, ran):
        self.name = name   # 이름
        self.num = num     # 학번
        self.grade1 = grade1 # 중간
        self.grade2 = grade2 # 기말
        self.avg = avg  #평균
        self.ran = ran # 석차
        
  def st_info(self):
        print(self.name, self.num, self.grade1, self.grade2, self.avg, self.ran)
    
  def st_name_num(self, name, num):
        self.name = name
        self.num = num

  def st_grade1_grade2(self, grade1, grade2):
        self.grade1 = grade1
        self.grade2 = grade2

  def st_avg_ran(self, avg, ran):
        self.avg = avg
        self.ran = ran

stu1 = St("Gildong", "12345", "20", "40", "30", "5")
stu2 = St("kook", "12346", "50", "50", "50", "3")
stu3 = St("yoon", "1234567", "20", "80", "50", "2")

print(stu1.name) # 출력물:  Gildong
print(stu2.name) # 출력물:  kook
                   
stu1.st_info() # 출력물: Gildong 12345 20 40 30 5
stu1.st_info() # 출력물: kook 12346 50 50 50 3
