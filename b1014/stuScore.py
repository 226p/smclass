# 학생성적프로그램 / 딕셔너리 타입으로 구현할 것
students = [
  {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
  {"no":2,"name":"유관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
  {"no":3,"name":"이순신","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
  {"no":4,"name":"강감찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
  {"no":5,"name":"김구","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
]

# 학생성적프로그램에 필요한 전역변수
s_title = ['번호','이름','국어','영어','수학','합계','평균','등수']
choice = 0
chk = 0
count = 1
stuNo = len(students)
no=1;name="";kor=0;eng=0;math=0;total=0;avg=0;rank=0

# 함수-------------------------------------------------------------------------------------------
def title_program():     # 메뉴 출력 함수
    print("[ 학생성적프로그램 ]")
    print("-"*60)
    print("1. 학생성적 입력")
    print("2. 학생성적 출력")
    print("3. 학생성적 수정")
    print("4. 학생성적 검색")
    print("5. 학생성적 삭제")
    print("6. 등수처리")
    print("7. 학생성적 정렬")
    print("0. 프로그램 종료")
    print("-"*60)
    choice = input("원하는 번호를 입력하세요.(0.종료)>> ")
    return choice

def stu_input(stuNo):    # 학생성적 입력 함수 - 일반변수
        while True:
            print("[ 학생성적 입력 ]")
            # 학생성적 직접 추가
            no = stuNo + 1
            name = input(f"{no}번째 학생 이름을 입력하세요.(취소:0) >> ")
            if name == '0':
                print("성적입력을 취소하여 이전화면으로 돌아갑니다.")
                print()
                break
            kor = int(input("국어 점수를 입력하세요."))
            eng = int(input("영어 점수를 입력하세요."))
            math = int(input("수학 점수를 입력하세요."))
            total = kor+eng+math
            avg = total/3
            rank = 0

            ss = {"no":no, "name":name, "kor":kor, "eng":eng, "math":math, "total": total, "avg":avg, "rank":0}
            students.append(ss)
            stuNo += 1
            print(f"{name}의 성적이 정상적으로 입력되었습니다.")
            print()
        return stuNo   # while문 종료시킬 수 있어 while문 밖에 써야 함

# ----------------------------------------------------------------------------------------------

# 학생성적프로그램
while True:
    choice = title_program()    # 함수호출 - 메뉴
    if choice == '1':
        stuNo = stu_input(stuNo)    # 함수호출 - 학생성적 입력

    elif choice == '2':
        print("                     [ 학생성적 출력 ]")
        for title in s_title:
            print(f"{title}\t", end="")  # 상단 타이틀 출력
        print()
        print("-"*60)
        for s in students:
            print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
        print()

    elif choice == '3':
        print("[ 학생성적 수정 ]")
        name = input("찾고자 하는 학생의 이름을 입력해주세요. >>")
        chk = 0
        for s in students:
          if s['name'] == name:
            print(f"{name} 학생의 정보를 찾았습니다.")
            print("[과목선택]")
            print("1. 국어점수")
            print("2. 영어점수")
            print("3. 수학점수")
            print("0. 뒤로가기")

            choice = input("수정할 과목 번호를 입력하세요. >>")
            if choice == '1':
                print(f"현재 국어점수 : {s['kor']}")
                s['kor'] = int(input("변경 국어점수 입력 >>"))
            elif choice == '2':
                print(f"현재 영어점수 : {s['eng']}")
                s['eng'] = int(input("변경 영어점수 입력 >>"))
            elif choice == '3':
                print(f"현재 수학점수 : {s['math']}")
                s['math'] = int(input("변경 수학점수 입력 >>"))
            elif choice == '0':
                print("성적 수정을 취소하여 이전 화면으로 돌아갑니다.")
                chk = 1

            if choice != '0':        # 변경된 점수 합계, 평균에 최신화
                s['total'] = s['kor']+s['eng']+s['math']
                s['avg'] = s['total']/3
                chk = 1

        # 없을 경우
        if chk == 0:
         print("수정하고자 하는 학생이름이 없습니다.")
         print()
    

    elif choice == '4':
        print("[ 학생성적 검색 ]")
        name = input("찾고자 하는 학생의 이름을 입력해주세요.")
        chk = 0
        for s in students:
            if s['name'] == name:
                print(f"{name} 학생의 정보를 찾았습니다.")
                print("                     [ 학생성적 출력 ]")
                for title in s_title:
                    print(title, end="\t")  # 상단 타이틀 출력
                print()
                print("-"*60)
                # 검색한 학생의 데이터 출력
                print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
                print()

    elif choice == '5':
        print("[ 학생성적 삭제 ]")
        name = input("찾고자 하는 학생의 이름을 입력해주세요.")
        chk = 0
        for idx,s in enumerate(students):
            if s['name'] == name:
                choice = input(f"{name} 학생의 정보를 찾았습니다. 학생의 성적을 삭제하겠습니까?\n(삭제 시 복구불가\t1.삭제 0.취소)")
                chk = 1
                if choice == '1':
                    del students[idx]
                    print(f"{name} 학생의 성적이 정상적으로 삭제되었습니다.")
                else:
                    print("학생성적 삭제가 취소되어 이전 화면으로 돌아갑니다.")
                    break

    elif choice == '6':
        print("[ 등수처리 ]")
        for s in students:
            count = 1
            for st in students:
                if s['total']<st['total']:
                    count += 1
                s['rank'] = count
        print("등수처리가 완료되었습니다.")
        print()

    elif choice == '7':
        while True:
            print("[ 학생성적 정렬 ]")
            print("1. 이름 순차정렬")      # sort 
            print("2. 이름 역순정렬")      # sort(,reverse=True)
            print("3. 합계 순차정렬")
            print("4. 합계 역순정렬")
            print("5. 번호 순차정렬")
            print("0. 이전 페이지 이동")
            print("-"*40)
            choice = input("원하는 번호를 입력하세요.(취소:0) >>")

            if choice == '1':
                students.sort(key=lambda x:x['name'])
            elif choice == '2':
                students.sort(key=lambda x:x['name'],reverse=True)
            elif choice == '3':
                students.sort(key=lambda x:x['total'])
            elif choice == '4':
                students.sort(key=lambda x:x['total'],reverse=True)
            elif choice == '5':
                students.sort(key=lambda x:x['no'])
            elif choice == '0':
                print("이전 페이지로 이동합니다.")
                break
            print("정렬이 완료되었습니다.")

            if choice == '0':
                print("정렬을 취소하여 이전 페이지로 돌아갑니다.")

    elif choice == '0':
        print("[ 프로그램 종료 ]")
        print("프로그램을 종료합니다.")
        break