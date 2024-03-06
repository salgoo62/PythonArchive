#3.1연산자_산술연산자
print(1+1)
print(3-2)
print(5*3)
print(6/3)

print(2**3)
print(10%3)
print(10//3)

#비교연산자
print(10>3)
print(4>=7)
print(10<3)
print(5<=5)

print(3==3)
print(4==2)
print(3+4==7)
print(1!=3)

#논리연산자
print((3>0) and (3>5))
print((3>0) or (3>5))
print(not(1!=3))

print(5>4>3)
print(4>5>3)

#연산자 우선순위
print(2+3*4)
print((2+3)*4)

#3.3 변수로 연산
number=2+3*4
print(number)
#number=number+2 #(2+3*4)+2
#print(number)
number += 2 #number=number+2와 동일
print(number)

#3.4 함수로 연산
print(abs(-5)) #절대값
print(pow(4,2)) #제곱한 값
print(max(5,12))
print(min(5,12))
print(round(3.12)) #소수점 이하 첫 자리에서 반올림
print(round(4.678,2)) #셋째 자리

#math모듈
from math import *

result=floor(4.99)
print(result) #4.99의 내림
result=ceil(3.14)
print(result) #3.14의 올림
result=sqrt(16)
print(result) #16의 제곱근

import math
result=math.floor(4.99)

#random모듈
from random import *
print(random())

print(random() * 10)
print(int(random()*10))
print(int(random()*10)+1)

print(randrange(1,46)) #1이상 46미만에서 난수
print(randint(1,45)) #1이상 45이하

#로또번호 6개추첨
print(randint(1,45))
print(randint(1,45))
print(randint(1,45))
print(randint(1,45))
print(randint(1,45))
print(randint(1,45))

#실습문제 스터디 날짜 정하기
from random import *
date=randint(4,28)
print("오프라인 스터디 모임 날짜는 매월"+str(date)+"일로 선정됐습니다.")


























