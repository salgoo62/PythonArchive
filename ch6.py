#5.1 리스트
#141
#지하철 칸별로 10명,20명,30명 승차
subway1=10
subway2=20
subway3=30
subway=[10,20,30]
print(subway)

subway=["푸","피글렛","티거"]
print(subway)

#피글렛이 몇 번째 칸에 탔는가?_인덱스 활용
print(subway.index("피글렛"))
#이요르 탑승
subway.append("이요르")
print(subway)

#루를 푸와 피글렛 사이(인덱스 1위치)에 삽입
subway.insert(1,"루")
print(subway)

#지하철 역마다 한 명씩 내림
print(subway.pop()) #이요르 내림
print(subway)

print(subway.pop()) #티거 내림
print(subway)

print(subway.pop()) #피글렛 내림
print(subway)

#지하철에서 모두 내림
subway.clear()
print(subway)

#중복값확인_같은 이름이 몇 명 있는지 확인
subway=["푸","피글렛","티거"]
subway.append("푸") #푸 추가
print(subway)
print(subway.count("푸"))

#리스트 정렬
num_list=[5,2,4,3,1]
num_list.sort() #오름차순 정렬
print(num_list)

num_list.sort(reverse=True) #내림차순 정렬
print(num_list)

num_list.reverse() #순서 뒤집기
print(num_list)

#리스트 확장
mix_list= ["푸",20,True]
num_list=[5,4,3,2,1]
num_list.extend(mix_list) #리스트 합치기
print(mix_list)
print(num_list)

#5.2딕셔너리
cabinet={3: "푸", 100: "피글렛"}
print(cabinet[3]) #key 3에 해당하는 value
print(cabinet[100]) #key 100에 해당하는 value

print(cabinet.get(3)) #key3에 해당하는 value
print(cabinet.get(5))
print("hi")

print(cabinet.get(5,"사용 가능")) #key에 해당하는 값이 없으면 기본값을 사용하게 함
print(3 in cabinet)
print(5 in cabinet)

cabinet={"A-3":"푸","B-100":"피글렛"}
print(cabinet["A-3"])
print(cabinet["B-100"])

#값 변경, 추가, 삭제
cabinet={"A-3": "푸", "B-100": "피글렛"}
print(cabinet)
cabinet["A-3"]="티거" #key에 해당하는 값이 있을 때 -> 값 변경
cabinet["C-20"]="이요르" #key에 해당하는 값이 없을 때 -> 값 추가
print(cabinet)

del cabinet["A-3"] #key 'A-3'에 해당하는 값 삭제
print(cabinet)

print(cabinet.keys()) #key만 출력
print(cabinet.values()) #value만 출력
print(cabinet.items()) #key, value 한 쌍으로 출력

cabinet.clear() #값 전체 삭제
print(cabinet)






