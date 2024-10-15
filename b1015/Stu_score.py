# import S_func
from S_func import *


# 학생성적프로그램
while True:
    choice = title_program()    # 함수호출 - 메뉴
    if choice == '1':
      stuNo = stu_input(stuNo)    # 함수호출 - 학생성적 입력
    elif choice == '2':
      stu_output(students)    # 함수호출 - 학생성적 출력
    elif choice == '3':
      stu_update(students)    # 함수호출 - 학생성적 수정
    elif choice == '4':
      stu_search(students)    # 함수호출 - 학생성적 검색
    elif choice == '5':
      stu_delete(students)    # 함수호출 - 학생성적 삭제
    elif choice == '6':
      stu_rank(students)    # 함수호출 - 등수처리
    elif choice == '7':
      stu_sort(students)    # 함수호출 - 학생성적 정렬

    elif choice == '0':
        print("[ 프로그램 종료 ]")
        print("프로그램을 종료합니다.")
        break