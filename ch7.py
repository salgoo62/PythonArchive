#튜플
menu =("돈가스", "치즈돈가스")
print(menu[0])
print(menu[1])

name = "피글렛"
age = 20
hobby = "코딩"
print(name,age,hobby)

(departure, arrival) = ("김포","제주")
print(departure, ">",arrival)
(departure, arrival) = (arrival,departure)
print(departure, ">",arrival)

#세트
my_set = {1,2,3,3,3}
print(my_set)
java = {"푸", "피글렛" , "티거"}
python = set(["푸","이요르"])

print(java & python)
print(java.intersection)
print(java|python)
print(java.union(python))
print(java-python)
print(python)

java.remove("피글렛")
print(java)

#자료구조 변환
menu = {"커피","우유","주스"}
print(menu)
print(type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu,type(menu))

menu = set(menu)
print(menu,type(menu))

#실습문제
from random import*
users = range(1,21)
users =  list(users)
shuffle(users)
winners = sample (users,4)
print("--당첨자 발표--")
print("치킨 당첨자: {0}".format(winners[0]))
print("커피 당첨자: {0}".format(winners[1:]))
print("--축하합니다!--")