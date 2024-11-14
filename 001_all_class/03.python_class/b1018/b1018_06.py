class Student:
  # 인스턴스 변수 - 객체선언을 하면 변수는 개별적으로 생성
  # 인스턴스 변수    참조변수.변수명, 참조변수명.함수명
  # 클래스 변수    클래스명.변수명, 클래스명,함수명

  count = 0    # 클래스변수 - 모든 객체가 동일한 변수를 사용
  students = []


  # 클래스 함수
  @classmethod
  def stu_print(cls):
    print(*s_title,sep='\t')  # 전개연산자(*)
    print("-"*60)
    for s in cls.students:
      print(str(s))

  def __init__(self,name,kor,eng,math):
    Student.count += 1
    self.no = Student.count    # 클래스변수 - 공용으로 변수 사용
    self.name = name
    self.kor = kor
    self.eng = eng
    self.math = math
    self.total = kor+eng+math
    self.avg = (kor+eng+math)/3
    self.rank = 0

    Student.students.append(self)   # Class

  def __str__(self):   # 객체를 문자열로 리턴함수 - 리턴은 항상 문자열이 되어야함.
    return f"{self.no}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg:.2f}\t{self.rank}"
    
  
  def print(self):    # 딕셔너리 타입으로 저장
    return {"no":self.no, "name":self.name,\
            "kor":self.kor, "eng":self.eng, "math":self.math,\
            "total":self.total, "avg":self.avg, "rank":self.rank}

# s1 = Student()
# s1.students
# s2 = Student()
# s1.students

s_title = ['번호','이름','국어','영어','수학','합계','평균','등수']
s_t = ["no","name","kor","eng","math","total","avg","rank"]

#### 학생성적 프로그램--------------------------------------------------------------
while True:
  print("[ 학생성적 프로그램 ]")
  print("1. 학생성적 입력")
  print("2. 학생성적 출력")
  print("3. 학생성적 비교")
  choice = int(input("원하는 번호를 입력하세요. >>"))

  if choice == 1:
    print("[ 학생성적 입력 ]")
    name = input("이름을 입력하세요. >>")
    score = []
    for i in range(2,5):
      score.append(int(input(f"{s_title[i]}점수를 입력하세요. >>")))
    s1 = Student(name,*score)
    # s1 = Student(name,*score)  # score[0],score[1],score[2]

    # 클래스변수 접근 방법
    for s in Student.students:
      print(s)

  elif choice == 2:
    print("[ 학생성적 출력 ]")
    Student.stu_print()   # 클래스 함수 호출

  elif choice == 3:
    print("[ 학생성적 비교 ]")
    while True:
      s1 = Student("홍길동",100,100,90)
      s2 = Student("유관순",90,100,90)
    
      





# students.append(s1.print())
# s2 = Student("유관순",90,90,99)
# students.append(s2.print())
# print(students)

# s1 = Student("홍길동",100,100,90)
# s2 = Student("유관순",90,90,99)
# print(s1.name)
# print(s1.count)
# print(s2.name)
# print(s2.count)
# print(s1.count)