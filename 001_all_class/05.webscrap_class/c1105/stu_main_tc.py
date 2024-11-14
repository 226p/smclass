import oracledb
import stu_func_tc

while True:
  choice = stu_func_tc.main_print() ## 메인 화면 출력
  if choice == "1":
    stu_func_tc.stu_insert() ## 학생성적 입력
  elif choice == "2":
    stu_func_tc.stu_output() ## 학생 성적 출력
  elif choice == "3":
    stu_func_tc.stu_select() ## 학생 성적 검색
  elif choice == "4":
    stu_func_tc.stu_sort() ## 학생 성적 정렬
  elif choice == "5":
    stu_func_tc.stu_rank() ## 등수 처리
  elif choice == "0":
    print("프로그램을 종료합니다.")
    break







