class Circle:
  def __init__(self,length):
    self.__length = length    # __ : 내부클래스만 변수에 접근해서 수정이 가능함(내부적캡슐화/접근제한)

  def get_area(self):  
    return self.__length**2*3.14
  def get_circum(self):
    return self.__length*2*3.14

  def get_length(self):
    return self.__length
  
  def set_length(self,length):
    self.__length = length 

  # 참조변수를 출력할 때 리턴되는 함수
  def __str__(self):
    c_str = "원의 반지름 : {}, 원의 넓이 : {}, 원의 둘레: {:.2f}".format(self.__length,self.get_area(),self.get_circum())
    return c_str

c1 = Circle(10)                      # 1. 선언 - 값을 입력
print(c1)
# print("길이 :",c1.get_length())        # 2. getter 값출력
# c1.set_length(200)                     # 3. setter 입력
# print("길이변경 :",c1.get_length())    # 4. getter 값출력
# c1.__length = 100                      # 5. 변수 직접입력
# print("직접변경 :",c1.__length)           # 6. 변수 직접출력
# print("get 읽어온 length",c1.get_length())  # 4. getter 값출력
