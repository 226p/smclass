class Student:
  count = 0
  chk = 0
  students = []

  @classmethod
  def stu_print(cls):
    print("[ 학생성적 출력 ]")
    print(*s_title,sep='\t')
    print("-"*60)
    for s in cls.students:
      print(s)


  def __init__(self,name,kor,eng,math):
    Student.count += 1
    self.no = Student.count
    self.name = name
    self.kor = kor
    self.eng = eng
    self.math = math
    self.total = kor+eng+math
    self.avg = (kor+eng+math)/3
    self.rank = 0

    Student.students.append(self)


  def __str__(self):
    return f"{self.no}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg}\t{self.rank}\t"
  
s_title = ['번호','이름','국어','영어','수학','합계','평균','등수']
s_t = ["no","name","kor","eng","math","total","avg","rank"]

###--------------------------------------------------



###--------------------------------------------------
while True:
  print("[ 학생성적 프로그램 ]")
  print("1. 학생성적 입력")
  print("2. 학생성적 출력")
  print("3. 학생성적 수정")
  print("0. 프로그램 종료")
  choice = int(input("원하는 숫자를 입력하세요. >>"))

  if choice == 1:
    print("[ 학생성적 입력 ]")
    name = input("이름을 입력하세요. >>")
    score = []
    for i in range(2,5):
      score.append(int(input(f"{s_title[i]}점수를 입력하세요. >>")))
    s1 = Student(name,*score)
  elif choice == 2:
    Student.stu_print()
  elif choice == 3:
    print("[ 학생성적 수정 ]")
    name = input("수정하고자 하는 학생의 이름을 입력하세요. >>")
    chk = 0
    for idx,s in enumerate(Student.students):
      if name == s.name:    # s[name] 위치값 찾기 ?? !
        print(f"{name} 학생의 정보를 찾았습니다.")
        chk = 1
    if chk == 0:
      print(f"{name} 학생의 정보가 없습니다. 다시 확인해주세요.")
  elif choice == 0:
    print("프로그램을 종료합니다.")
    break