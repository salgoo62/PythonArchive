#4.1문자열
sentence1 = '나는 소년입니다.'
print(sentence1)

sentence2 = "파이썬은 쉬워요."
print(sentence2)

sentence1 = '나는 소년입니다.'
print(sentence1,type(sentence1))

sentence2 = "파이썬은 쉬워요."
print(sentence2,type(sentence2))

sentence3 = """
나는 소년이고,
파이썬은 쉬워요.
"""
print(sentence3)

#4.2 슬라이싱
jumin = "990229-1234567"
print("성별 식별번호 :"+ jumin[7])

jumin = "990229-1234567"
print("연"+ jumin[0:2])
print("연"+ jumin[2:4])
print("연"+ jumin[4:6])

print("생년월일:"+ jumin[:6])
print("주민등록번호 뒷자리 :"+ jumin[7:])

print("주민등록번호 뒷자리(뒤에서부터):"+ jumin[-7])


#4.3 함수로 문자열정리
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(python[1:3].islower())
print(python.replace("python","java"))

python = "Python is Amazing"
find = python.find("n")
print(find)
find = python.find("n",find + 1)
print(find)
find = python.find("java")
print(find)


index = python.index("n")
print(index)
index = python.index("n",index + 1)
print(index)
index = python.index("n",2,6)
print(index)


python = "Python is Amazing"
print(python.count("n"))
print(python.count("v"))
print(len(python))




