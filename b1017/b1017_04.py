print("프로그램을 시작합니다.")
print("1")
print("2")
try:
  print("3")
  print("4")
  raise NotImplementedError("프로그램을 구현해야 함")    # 프로그램을 구현되어 있지 않음(강제에러)
  print("5")
except Exception as e:
  print("6")
  print("7")
finally:
  print("8")
  print("9")
print("10")
print("프로그램을 종료합니다.")


# list_1 = [52,273,32,72,100]

# try:
#   n_input = int(input("정수를 입력하세요. >>"))
#   print(f"{n_input}는 리스트의 {list_1[n_input]}")

# except ValueError as e:
#   print("값을 잘못 입력하였습니다.",type(e),e)

# except IndexError as e:
#   print("번호가 범위를 벗어났습니다.",type(e),e)

# except Exception as e:
#   print("모든 예외처리의 부모")

# Exception 모든 예외 부모, 상위 객체(클래스)
# as e : e변수는 예외에 대한 설명문, type(e) : 예외객체
# 리스트 범위 밖 호출 에러 : IndexError
# 입력된 값의 변환 에러 : ValueError
# 강제예외 발생 : raise