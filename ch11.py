#기본값 사용
def profile(name, age=20, main_lang="파이썬"):
    print("이름: {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))

profile("찰리")
profile("루시")

#가변인자 사용
def profile(name, age, *language):
    print("이름:{0}\t나이:{1}\t".format(name, age), end=" ")
    #print(language, type(language))
    for lang in language:
        print(lang, end=" ") #언어를 모두 한 줄에 표시
    print() #줄 바꿈 목적
#자바스크립트 추가
profile("찰리", 20, "파이썬", "자바", "C", "C++", "C#","자바스크립트")
profile("루시", 25, "코틀린", "스위프트")

#7,4 변수의 범위: 지역변수와 전역 변수
glasses = 10 #전체 30 안경 개수:10개

def rent_return(glasses, people): #전체 30안경 수와 대여한 관객 수를 전달받음
    glasses=glasses-people #잔여 30 안경 개수=전체 개수-대여한 개수
    print("[함수 내부]남은 30 안경 개수: {0}".format(glasses))
    return glasses
print("전체 30안경 개수: {0}".format(glasses))
glasses=rent_return(glasses,2) #함수 안에서 수정된 glasses 값을 반환
print("남은 30 안경 개수: {0}".format(glasses))

#실습문제_표준체중계싼
def std_weight(height,gender): 
    if gender =="남자":
        return height*height*22
    else:
        return height*height*21
height=175
gender="남자"
#weight=std_weight(height/100,gender)
weight=round(std_weight(height/100,gender),2)
print("키 {0}cm {1}의 표준 체중은 {2}kg입니다.".format(height,gender,weight))
