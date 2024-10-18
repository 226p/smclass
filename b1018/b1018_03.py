#### 클래스 생성
class Car:     # 생성자 없으면 기본생성자로 
  def __init__(self,color,speed,tire,gear):
    self.color = color  # 변수
    self.__speed = speed
    self.tire = tire
    self.gear = gear

  def upSpeed(self,value):    # 함수
    if value > 0: self.__speed += value
    else:
      raise "값을 잘못 넣었습니다."

  def downSpeed(self,value):
    self.__speed -= value

#### 클래스 선언(클래스 사용)
c1 = Car("white",0,4,"auto")
c1.color = "blue"
print(c1.color)
c1.speed = 300
print(c1.speed)

# c1 = Car()
# c1.speed = 200
# print(c1.speed)
# print(c1.tire)

# c2 = Car()
# c2.color = "red"
# print(c2.color)

# 리스트, 딕셔너리 변수 직접 값을 할당하는 방식(보안취약)

# speed 변수에 직접 값을 할당(속도 = 0 -> 100) but 값을 컨트롤할 수 없음(해킹가능)
# c1.speed = 100
# print(c1.speed)

# 함수를 활용하여 값을 할당(속도 = 0 -> 100) 권장 !!
# c1.upSpeed(100)
# print(c1.speed)
