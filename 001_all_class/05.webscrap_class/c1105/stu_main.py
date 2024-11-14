import oracledb
import stu_func



while True:
  print("[ 학생성적프로그램 ]")
  print("1. 학생성적 입력")
  print("2. 학생성적 출력")
  print("3. 학생성적 검색")
  print("4. 학생성적 정렬")
  print("5. 등수처리")
  print("0. 프로그램 종료")
  print()
  choice = input("원하는 번호를 입력하세요. >>")

  if choice == '1':
    stu_func.stu_input()

  elif choice == '2':
    stu_func.stu_output()

  elif choice == '3':
    stu_func.stu_search()

  elif choice == '4':
    stu_func.stu_order()
    
  elif choice == '5':
    stu_func.stu_rank()

  elif choice == '0':
    print("프로그램을 종료합니다.")
    break 




