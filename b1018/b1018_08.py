class Student:
  count = 0       # 클래스변수
  students = []

  @classmethod
  def stu_print(cls):
    for s in cls.students:
      print(s)

  def __init__(self,name,kor,eng,math):
    Student.count += 1
    self.no = Student.count   # 클래스 변수
    self.name = name          #  인스턴스 변수
    self.kor = kor
    self.eng = eng
    self.math = math
    self.total = kor+eng+math
    self.avg = (kor+eng+math)/3
    self.rank = 0

    Student.students.append(self)

  def __str__(self):      # 객체선언 한 참조변수 출력하면 주소값이 출력됨.  0x000 -> __str__ 로 변경
    return f"{self.no}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg}\t{self.rank}"

#### 데이터,변수를 보호하는 방법(__ : private) - no getter를 사용하지 않으면 접근 불가
#   def __init__(self):
#     self.__no = 10

#   def get_no(self):
#     return self.__no 
#   def set_no(self,no):
#     if no<10 : raise "0이하는 입력할 수 없습니다."
#     self.__no = no

# s1 =Student()
# s1.set_no(-100)
# print(s1.get_no())
#----------------------------------------------------------------------------------

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
    s1 = Student(name,*score)  # 객체선언

  if choice == 2:
    print("[ 학생성적 출력 ]")
    print(*s_title,sep='\t')
    print("-"*60)
    Student.stu_print()   # 클래스함수 호출

      
