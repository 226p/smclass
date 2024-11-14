def operate(count):
  for i in range(count):
      print("한국어 인사 : 안녕하세요")
  # pass 에러를 방지하기 위해 사용하는 의미없는 용어

while True:
  print("[ 외국어 인사 ]")
  print("1. 영어 인사")
  print("2. 일본어 인사")
  print("3. 중국어 인사")
  print("4. 불어 인사")
  choice = input("원하는 번호를 입력하세요. >>")
  count = int(input("한국어 반복횟수를 입력하세요. >>"))    # 매개변수

  if choice == '1':
    operate(count)      # 함수호출
    print("영어 인사 : Hello(헬로우)")

  elif choice == '2':
    operate(count)
    print("일본어 인사 : Ohayo(오하이요)")

  elif choice == '3':
    operate(count)
    print("중국어 인사 : Ni hau(니하오)")

  elif choice == '4':
    operate(count)
    print("불어 인사 : Bonjour(봉주르)")


