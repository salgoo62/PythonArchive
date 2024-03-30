#사용자 정의 예외 처리하기
class BigNumberError(Exception):
    def __init__(self,msg):
        self.msg=msg

    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1=int(input("첫 번째 숫자를 입력하세요 :"))
    num2=int(input("두 번째 숫자를 입력하세요 :"))
    if num1 >= 10 or num2 >= 10: #입력받은 수가 한 자리인지 확인
        raise ValueError
    print("{0}/{1}={2}".format(num1,num2,int(num1/num2)))
except ValueError:
    print("값을 잘못 입력했습니다. 한 자리 숫자만 입력하세요")
except BigNumberError as err:
    print("오류가 발생했습니다.한 자리 숫자만 입력하세요.")
    print(err)
finally: #오류 발생 여부와 상관없이 항상 실행
    print("계산기를 이용해 주셔서 감사합니다.")

#실습문제
class SoldOutError(Exception):
    pass

chicken=10 #남은 치킨 수
waiting=1 #대기번호, 1부터 시작

while True:
    try:
        print("[남은 치킨: {0}]".format(chicken))
        order = int(input("치킨을 몇 마리 주문하시겠습니까?"))
        if order > chicken: #남은 치킨보다 주문량이 많을 때
            print("재료가 부족합니다.")
        elif order <= 0:
            raise ValueError
        else:
            print("[대기번호 {0}] {1}마리를 주문했습니다.".format(waiting,order))
            waiting += 1 #대기번호 증가
            chicken -= order # 주문 수만큼 남은 치킨 감소
        if chicken == 0:
            raise SoldOutError
    except ValueError:
        print("잘못된 값을 입력했습니다")
    except SoldOutError:
        print("재료가 소진돼 더 이상 주문을 받지 않습니다.")
        break