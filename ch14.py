#게임 소개
#보병: 공격 유닛, 군인, 총을 쏠 수 있음
name="보병" #이름
hp=40 #체력
damage=5 #공격력

print("[]유닛을 생성했습니다.".format(name))
print("체력{0}, 공격력{1}\n".format(hp,damage))

#탱크: 공격 유닛, 포를 쏠 수 있음, 두가지모드 (일반/시저 모드)
tank_name="탱크"
tank_hp=150
tank_damage=35

print("{}유닛을 생성했씁니다.".format(tank_name))
print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

#새로운 탱크2추가
tank2_name="탱크"
tank2_hp=150
tank2_damage=35

print("{} 유닛을 생성했습니다.".format(tank_name))
print("체력{0}, 공격력 {1}\n".format(tank2_hp, tank2_damage))

#공격함수
def attack(name, location, damage):
    print("{0}:{1} 방향 적군을 공격합니다. [공격력 {2}]".format(name,location, damage))

attack(name,"1시",damage) #보병 공격 명령
attack(tank_name, "1시", tank_damage) #탱크 공격 명령
attack(tank2_name, "1시", tank2_damage) #탱크2 공격 명령

#클래스와 객체 생성하기
class Unit:
    def __init__(self,name,hp,damage):
        self.name=name #인스턴스 변수 name에 전달값 name 저장
        self.hp=hp #인스턴스 변수 hp에 전달값 hp저장
        self.damage=damage #인스턴스 변수 damage에 전달값 damage 저장
        print("{0}유닛을 생성했습니다.".format(self.name))
        print("체력{0}, 공격력{1}".format(self.hp, self.damage))


#전투기 :공중 유닛, 은폐 불가
stealth1=Unit("전투기",80,5) #체력80, 공격력5
#인스턴스 변수 접근
print("유닛 이름: {0}, 공격력:{1}".format(stealth1.name, stealth1.damage))

#은폐 가능
stealth2=Unit("업그레이드한 전투기",80,5)
#업그레이드한 전투기만을 위한 특별한 인스턴스 변수 정의, 은폐 상태
stealth2.cloaking=True

if stealth2.cloaking == True: #은폐 상태라면
    print("{0}는 현재 은폐 상태입니다.".format(stealth2.name))


#메서드
class AttackUnit: #공격유닛
    def __init__(self, name, hp, damage):
        self.name=name
        self.hp=hp
        self.damage=damage

    def attack(self, location): #전달받은 받향으로 공격
        print("{0}:{1} 방향 적군을 공격합니다. [공격력{2}]"\
              .format(self.name, location, self.damage)) #공간이 좁아서 2줄로 나눔
        
    def damaged(self,damage): #damage만큼 유닛 피해
        #피해 정보 출력
        print("{0}:{1}만큼 피해를 입었습니다.".format(self.name,damage))
        self.hp-=damage #유닛의 체력에서 전달받은 damage만큼 감소
        #남은 체력 출력
        print("{0}:현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp<=0: #남은 체력이 0이하이면
            print("{0}:파괴됐습니다.".format(self.name)) #유닛 파괴 처리

#화염방사병:공격유닛, 화염방사기를 사용함
flamethrower1=AttackUnit("화염방사병", 50, 16) #객체 생성, 체력50, 공격력 16
flamethrower1.attack("5시") #5시 방향으로 공격 명령

#25만큼의 공격을 2번 받음
flamethrower1.damaged(25) #남은 체력 25
flamethrower1.damaged(25) #남은 체력 0