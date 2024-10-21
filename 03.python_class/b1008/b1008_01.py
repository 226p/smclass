students = []    
no = 1
name = ""; kor = 0; eng = 0; math = 0; total = 0; avg = 0; rank = 0
chk = 0
stuNo = 0
stuNo = len(students)
s_title = ["번호","이름","국어","영어","수학","합계","평균","순위"]


while True:
  print("[ 학생성적프로그램 ]")
  print("-"*60)
  print("1. 학생성적 입력")
  print("2. 학생성적 출력")
  print("3. 학생성적 수정")
  print("4. 학생성적 검색")
  print("5. 학생성적 삭제")
  print("6. 등수처리")
  print("0. 프로그램 종료")
  print("-"*60)
  choice = input("원하는 번호를 입력하세요.(0.종료)>> ")

  if choice == '1':
    while True :
      print("[ 학생성적 입력 ]")
      no = stuNo + 1
      name = input(f"{no}번째 학생 이름을 입력하세요.(취소 : 0) >>")
      if name == '0':
        print("학생 성적 입력을 취소합니다. 이전 화면으로 돌아갑니다.")
        break
      kor = int(input("국어 점수를 입력하세요."))
      eng = int(input("영어 점수를 입력하세요."))
      math = int(input("수학 점수를 입력하세요."))
      total = kor+eng+math
      avg = total/3
      rank = 0
      students.append([no,name,kor,eng,math,total,avg,rank])
      stuNo += 1
      print(f"{no}번째 성적 입력이 완료되었습니다.")

  if choice == '2':
    print("                      [ 학생성적 출력 ]")
    for title in s_title:
      print(f"{title}\t",end='')
    print()
    print("-"*60)
    for s in students:
      print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}")

  if choice == '3':
    print("[ 학생성적 수정 ]")
    name = input("수정할 학생의 이름을 입력해주세요.(취소 : 0) >>")
    chk = 0
    for s in students:
      if s[1] == name:
        print(f"{name} 학생의 정보를 찾았습니다.")
        print("1. 국어점수")
        print("2. 영어점수")
        print("3. 수학점수")
        choice = input("수정할 과목을 선택하세요. >>")
        if choice == '1':
          print("이전 국어점수 : {}".format(s[2]))
          s[2] = int(input("변경 국어점수 : "))
        elif choice == '2':
          print("이전 영어점수 : {}".format(s[3]))
          s[3] = int(input("변경 영어점수 : "))
        elif choice == '3':
          print("이전 수학점수 : {}".format(s[4]))
          s[4] = int(input("변경 수학점수 : "))
        s[5] = s[2]+s[3]+s[4]
        s[6] = s[5]/3
        print("수정이 완료되었습니다.")
        print("                      [ 학생성적 출력 ]")
        for title in s_title:
          print(f"{title}\t",end='')
        print()
        print("-"*60)
        for s in students:
          print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}")
        chk = 1
      elif name == '0':
        print("수정을 취소합니다. 이전 화면으로 돌아갑니다.")
        chk = 1
        break
    if chk == 0:
      print("해당 학생의 정보가 없습니다. 다시 확인해주세요.")
    
  elif choice == '4':
    print("[ 학생성적 검색 ]")
    name = input("검색할 학생의 이름을 입력해주세요. >>")
    chk = 0
    for s in students:
      if s[1] == name:
        chk = 1
        print(f"{name} 학생의 정보를 찾았습니다.")
        print("                      [ 학생성적 출력 ]")
        for title in s_title:
          print(f"{title}\t",end='')
          print()
          print("-"*60)
        for s in students:
          print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}")
          print()
