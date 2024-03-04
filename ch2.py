#2.1 숫자자료형
print(5)

print(-10)
print(3,14)
print(1000)

print(5+3)
print(2*8)
print(6/3)
print(3*(3+1))

#2.2 문자열 자료형
print('풍선')
print("나비")
print("abcdefg")
print("10")
print("파이썬"*3)
#print('작은따옴표")
#print("큰따옴표')

#2.3 불 자료형      
print(5>10)
print(5<10)

print(True)
print(False)

print(not True)
print(not False)

not(5>10)
print(not(5>10))

#2.4변수
print("반려동물을 소개해 주세요")
print("우리 집 반려동물은 개인데, 이름이 연탄이예요")
print("연탄이는 4살이고, 산책을 아주 좋아해요.")
print("연탄이는 수컷인가요?")
print("네.")

name="해피"
animal="고양이"
age=4
hobby="낮잠"
is_male=True

print("반려동물을 소개해 주세요")
print("우리 집 반려동물은 개인데, 이름이 연탄이예요")
print("연탄이는 4살이고, 산책을 아주 좋아해요.")

#문자열과 변수가 문장 안에 같이 있을 때 +연산자로 연결
#"문자열"+변수+"문자열"
print("반려동물을 소개해 주세요")
print("우리 집 반려동물은 "+animal+"인데, 이름이 "+name+"예요.")
hobby="수영" 
#print(name+"는 "+age+"살이고,"+hobby+"을 아주 좋아해요.") #에러
print(name+"는 "+str(age)+"살이고, "+hobby+"을 아주 좋아해요.")

#형변환
print(int("3"))
#print(int("3")+"입니다.") #에러
print(int(3.5)) 
#print(int("삼")) #에러 #int는 오로지 숫자만 

print(float("3.5"))
print(float(3))

#print(float("오")) #에러 float도 오로지 숫자만

print(str(3)+"입니다.")
print(str(3.5)+"입니다.")

#자료형 확인 type()
print(type(3)) #정수(int)
print(type("3")) #문자열(str)
print(type(3.5)) #실수(float)
print(type(str(3))) #정수를 문자열로 형변환

#2.5 주석
#command+/

#2.6 실습 문제:역 이름 출력하기
station="인천공항"
print(station+"행 열차가 들어오고 있습니다")

#셀프체크
status="배송 완료"
print("주문상태 : ", status)
