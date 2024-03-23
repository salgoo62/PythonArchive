#파일 입출력
#score.txt 파일을 쓰기 모드로 열기
score_file=open("score.txt","w",encoding="utf8")
print("수학:0", file=score_file) #score.txt 파일에 내용 쓰기
print("영어:50",file=score_file) #score.txt 파일에 내용 쓰기
score_file.close() #score.txt파일 닫기

#score.txt파일에 이어쓰기 모드로 열기
score_file=open("score.txt","a",encoding="utf8")
#write()함수는 줄 바꿈이 없으므로 \n 추가
score_file.write("과학:80\n")
score_file.write("코딩:100\n")
score_file.close()

#score.txt 파일을 읽기 모드로 열기
score_file=open("score.txt","r",encoding="utf8")

lines=score_file.readlines() #파일에서 모든 줄을 읽어 와 리스트 형태로 저장
for line in lines: #lines에 내용이 있을 때까지
    print(line,end="") #읽어 온 내용 출력

score_file.close

#8.5데이터를 파일로 저장하기 : pickle모듈
import pickle 

profile_file=open("profile.pickle","wb") #바이너리 형태로 저장
profile={"이름": "스누피","나이":30,"취미":["축구","골프","코딩"]}
print(profile)

pickle.dump(profile,profile_file) #profile 데이터를 파일에 저장
profile_file.close() #파일닫기

profile_file=open("profile.pickle","rb") #읽어 올 때도 바이너리 형태 명시
profile=pickle.load(profile_file) #파일에 있는 정보를 불러와서 profile에 저장

print(profile)
profile_file.close()

#파일 한 번에 열고 닫기 : with문
import pickle

with open("study.txt","w",encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요.")

with open("study.txt","r",encoding="utf8") as study_file:
    print(study_file.read())

#실습문제 : 보고서 파일 만들기
    for i in range(1,51): #숫자 1~50
        with open(str(i) + "주차.txt","w",encoding="utf8") as report_file:
            report_file.write("-{0}주차 주간보고-".format(i))
            report_file.write("\n부서: ") #줄 바꿈 처리

