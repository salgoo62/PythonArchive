#4.4 문자열 포매팅
print("ab"+"ab")
print("ab","ab")

print("나는 %d살 입니다." % 20)
print("나는 %s을 좋아합니다." % "파이썬")
print("Apple은 %c로 시작해요."%"A")
print("나는 %s살입니다."%20) #%s로도 정숫값 표현 가능

print("나는 %s색과 %s색을 좋아해요." % ("파란","빨간")) #값이 여럿일 때

print("나는 {}살입니다." .format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란","빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란","빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란","빨간"))

print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color="빨간", age=20))
#값의 이름으로 직접 지정> 중괄호와 format함수에서 이름 순서가 달라도 상관없음

age=20
color="빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

#4.5 탈출문자
print("백문이 불여일견 백견이 불여일타")
print("백문이 불여일견\n백견이 불여일타")

print("저는 '김보해'입니다.")

#\r 커서를 맨앞으로 이동
print("Red Apple\rPine")
#\b 앞 글자 하나 제거
print("Redd\bApple")
#\t tab효과
print("Red\tApple")

#실습문제 : 비밀번호 만들기
url="http://naver.com"
my_str=url.replace("http://","")
my_str=my_str[:my_str.index(".")]
password=my_str[:3]+str(len(my_str))+str(my_str.count("e"))+"!"
print("{0}의 비밀번호는 {1}입니다.".format(url,password))

