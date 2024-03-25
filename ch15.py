class unit:
    def __init__(self,name,hp):
       self.name = name
       self.hp = hp 

#일반유닛
class unit:
    def __init__(self,name,hp):
        self.name = name
        self.hp = hp
#공격유닛
class attackunit(unit):
    def __init__(self, name, hp,damage):
        unit.__init__(self,name,hp) 
        self.damage = damage
        def attack(self,location):
            print("{0}:{1} 방향 적군을 공격합니다. [공격력{2}]"\
                .format(self.name,location,self.damage))
    def damaged(self,damage):
        #피해정보출력
        print("{0}:{1}만큼 피해를 입었습니다.".format(self.name,self,damage))
        self.hp -= damage
        #남은체력출력
        print("{0}:현재 체력은 {1}입니다.".format(self.name,self.hp))
        if self.hp <= 0:
          print("{0}:파고됐습니다.".format(self.name))
#flamethrower1 = attackunit("화염방사병,50,16")
#flamethrower1.attack("5시")

#flamethrower1.damaged(25)    
#flamethrower1.damaged(25)

#비행기능
class flyable:
    def __init__(self,flying_speed):
        self.flying_speed = flying_speed
        def fly(self,name,location):
            print("{0}:{1}방향으로 날아갑니다.[속도{2}]"\
                .format(name,location,self.flying_spped))
#공중 공격 유닛
class flyableattackunit(attackunit,flyable):
    def __init__(self,name,hp,damage,flying_speed):
        attackunit.__init__(self,name,hp,damage)
        flyable.__init__(self,flying_speed) 

    




#일반 유닛
class unit:
    def __init__(self, name, hp, speed): 
      self.name = name
      self.hp = hp
      self.speed= speed # 지상 이동 속도
def move(self, location):
    print("[지상 유닛 이동]")
    print("(0) : (1} 방향으로 이동합니다. [속도 (2)1"\
          .format(self.name, location, self.speed))


# 공격 유닛
class attackunit(unit):
 def __init__(self, name, hp, damage, speed): 
  unit.__init__(self, name, hp, speed) # speed ≥7
  self.damage = damage
def attack(self, location):
    print("{0}:{1}방향 적군을 공격합니다.[공격력{2}]"\
        .format(self.name,location,self.damage))
def damaged (self, damage):
    print("{O} : {1}만큼 피해를 입었습니다.".format(self.name, damage))
    self. hp -= damage
    print("{0}:현재 체력은 {1}입니다.".format(self.name,self.hp))
    if self.hp <=0:
        print("{0}:파괴됐습니다.".format(self.name))
#비행 기능
class flyable:
    def __init__(self,flying_speed):
        self.flying_speed = flying_speed 
        def fly(self,name,location):
            print("{0}:{1}방향으로 날아갑니다[속도{2}]"\
                .format(name,location,self.flying_speed))   
#공중 공격 유닛
class flyableattackunit(attackunit,flyable):
    def __init__(self,name,hp,damage,flying_speed):
        attackunit.__init__(self,name,hp,damage,0)
        fltable.__init__(self,flying_speed)
        def move(self,location):
            print("[공중 유닛 이동]")
            self.fly(self.name,location) 
hoverbike = attackunit("호버 바이크,80,20,10")
spacecruiser = flyableattackunit("우주 순양함,500,25,3")
hoverbike.move("11시")
spacecruiser.move("9시")                           
 



#건물 유닛
class buildingunit(unit):
    def __init__(self,name,hp,location):
        pass
    supply_depot = buildingunit("보급고",500,"7시")
def game_start():
    print("[알림]새로운 게임을 시작합니다.")
def game_over():
    pass
game_start
game_over

class unit:
    def __init__(self):
        print("unit 생성자")
class fltable:
    def __init__(self):
        print("flyable 생성자")
class flyableunit(flyable,unit):
    def __init__(self):
        unit.__init__(self)
        flyable.__init__(self)
        
troopship = flyableunit()