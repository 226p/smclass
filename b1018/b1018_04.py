#### 절차적인 형태의 프로그램 구현
# r = int(input("반지름을 입력해주세요. >>"))
# print("원의 넓이 :",r**2*3.14)
# print("원의 둘레 :",r*2*3.14)


class Circle:
  def __init__(self,r):
    self._r = r

  def get_area(self):    # __ : 내부클래스만 변수에 접근해서 수정이 가능함(접근제한)
    return self._r**2*3.14
  def get_circum(self):
    return self._r*2*3.14

c1 = Circle(int(input("반지름을 입력해주세요. >>")))

c1.r = 7
print("넓이 :",c1.get_area())
print("둘레 :",c1.get_circum())

c2 = Circle(int(input("반지름을 입력해주세요. >>")))
print("넓이 :",c2.get_area())
print("둘레 :",c2.get_circum())