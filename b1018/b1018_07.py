# a = [1,2,3]  # 전개연산자
# print(*a)

# s_title = ['번호','이름','국어','영어','수학','합계','평균','등수']

# print(*s_title,sep='\t')
class Student:
  count = 0    # 클래스변수 - 모든 객체가 동일한 변수를 사용
  students = []

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

  def __eq__(self, value):  # 특별 함수 == : 호출되는 함수(이꼬르)    self(현재자신 객체),value(비교할 다른 객체)
    return self.total == value.total
  
  def __ne__(self, value):  # 특별 함수 != : 호출되는 함수(not이꼬르)    self(현재자신 객체),value(비교할 다른 객체)
    return self.total != value.total
  
  def __gt__(self, value):  # 특별 함수 > : 호출되는 함수    self(현재자신 객체),value(비교할 다른 객체)
    return self.total > value.total
  
  def __ge__(self, value):  # 특별 함수 >= : 호출되는 함수    self(현재자신 객체),value(비교할 다른 객체)
    return self.total >= value.total
  
  def __lt__(self, value):  # 특별 함수 < : 호출되는 함수   self(현재자신 객체),value(비교할 다른 객체)
    return self.total < value.total
  
  def __le__(self, value):  # 특별 함수 <= : 호출되는 함수    self(현재자신 객체),value(비교할 다른 객체)
    return self.total <= value.total


s1 = Student("홍길동",100,100,100)  # 300
s2 = Student("유관순",90,100,100)  # 290

if (300>290):  # 숫자 비교
  print(True)
else:
  print(False)

if (s1 > s2):  # 객체 비교(특별함수 eq 발동)
  print(True)
else:
  print(False)

# if (s1 == s2):  # 객체 비교(특별함수 eq 발동)
#   print(True)
# else:
#   print(False)