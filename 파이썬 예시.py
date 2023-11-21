class Student(object):
  
    def __init__(self, name, dept, num, grade):
        self.name = name   # 이름
        self.dept = dept   # 학과
        self.num = num     # 학번
        self.grade = grade # 성적
        
    def get_student_info(self):      # 마찬가지로 첫번째 인자엔 self 가 들어와야함
        print(self.name, self.dept, self.num, self.grade)
    
    def set_stu_name(self, name):
        self.name = name
   
  
#### 아까와 같이 학생 객체를 만들어보자.

stu1 = Student("Gildong", "CS", "12345", 3.5)

print(stu1.name)   
# '.' 을 이용해서 속성을 출력할수 있다.
# 출력물:  Gildong
                   
stu1.get_student_info()    # class에서 정의한 함수를 호출하면 method를 사용하는 것임.
# 출력물: Gildong CS 12345 3.5 

stu1.set_stu_name('AAA')  # 객체의 이름이 AAA로 바뀐다.
stu1.get_student_info()   # 다시 메서드를 호출
# 출력물: AAA CS 12345 3.5
