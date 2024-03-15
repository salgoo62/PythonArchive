#7 함수
#은행계좌 개설하기
def open_account():
    print("새로운 계좌를 개설합니다.")
open_account() #앞에 정의한 open_account함수 호출

#입금하기
def deposit(balance,money): #입금처리함수
    print("{0}원을 입금했습니다. 잔액은 {1}원입니다.".format(money, balance+money))
    return balance+money #입금 후 잔액 정보 반환
#출금하기
def withdraw_night(balance,money): #업무 시간 외 출금ㄴ
    commision = 100 #출금 수수료 100원
    print("업무 시간 외에 {}원을 출금했습니다.".format(money))
    return commision, balance-money-commision
    
balance=0 #초기잔액
balance=deposit(balance,1000) #1,000원 입금

#업무 시간 외 출금 시도
commision, balance = withdraw_night(balance,500)
print("수수료 {0}원이며, 잔액은 {1}원입니다.".format(commision, balance))

name, age, hobby = "피글렛", 20, "코딩" #변수명에 소괄호가 없어도 실행결과는 동일
print(name,age,hobby)


