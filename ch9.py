#6.2반복문
print("대기번호:1")
print("대기번호:2")
print("대기번호:3")
print("대기번호:4")

for waiting_no in [1,2,3,4,5]:
    print("대기번호:{0}".format(waiting_no)) #{0}위치에 waiting_no의 값이 들어감

for waiting_no in range(5):
    print("대기번호:{0}".format(waiting_no))

for waiting_no in range(1,6):
    print("대기번호:{0}".format(waiting_no))

for waiting_no in range(1,6,2):
    print("대기번호:{0}".format(waiting_no))

orders=["아이언맨","토르","스파이더맨"] #손님 닉네임 리스트
for customer in orders:
    print("{0}님, 커피가 준비됐습니다. 픽업대로 와 주세요.".format(customer))

customer="토르" #손닉닉네임
index=5 #초깃값, 부르는 횟수 최대5번

while index>=1: #부르는 횟수가 1이상일 때만 실행
    print("{}님, 커피가 준비됐씁니다.".format(customer))
    index-=1 #횟수 1회 차감
    print("{}번 남았어요.".format(index))
    if index == 0: #5번 모두 불렀다면
        print("커피를 폐기 처분합니다.")

#customer="아이언맨"
#index=1

#while True:
    #print("{0}님, 커피가 준비됐습니다. 호출 {1}회".format(customer, index))
    #index+=1

#customer="토르"
#person=None

#çwhile person != customer:
    #print("{0}님, 커피가 준비됐습니다.".format(customer))
    #person=input("이름이 어떻게 되세요?")

#흐름 제어하기: continue와 break
absent=[2,5]  #결석한 학생 출석번호
no_book=[7] #책을 가져오지 않은 학생 출석번혼

for student in range(1,11): #출석번호 1~10번
    if student in absent: #결석한 학생이면 
        continue #다음 학생으로 넘어가기
    elif student in no_book: #책을 가져오지 않으면 바로 수업 종료
        print("오늘 수업은 여기까지. {0}번 학생은 교무실로 따라와요.".format(student))
        break #반복문 탈출
    print("{0}번 학생, 책을 읽어 보세요.".format(student))

#for문 한 줄로 작성하기
students=[1,2,3,4,5]
print(students)

#한 줄 for문으로 각 항목에 100 더하기
students=[i+100 for i in students]
print(students)

students=[students[0]+100, students[1]+100, students[2]+100, students[3]+100, students[4]+100]
students=[1+100, 2+100, 3+100, 4+100, 5+100]

students=["Iron man","Thor","Spider man"]
print(students)

#한 줄 for문으로 각 이름을 이름의 길이 정보로 변환
students=[len(i) for i in students]
print(students)

#한 줄 for문으로 각 이름을 모두 대문자로 변경
#students=[i.upper() for i in students]
#print(students)

#6.3 실습문제 : 택시 승객 수 구하기
from random import *

cnt=0
for i in range(1,51):
    time=randrange(5,51)
    if 5<=time<=15:
        print("[0] {0}번째 손님 (소요시간:{1}분)".format(i, time)) #매칭 성공 출력
        cnt+=1 #총 탑승객 수 증가 처리
    else:
        print("[ ] {0}번째 손님 (소요시간 :{1}분)".format(i,time)) #매칭 실패 출력
print("총 탑승객:{0}명".format(cnt))