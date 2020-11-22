print("비만도 계산하기")
print()
name=input("이름을 적어주세요")

   
print("비만도는 체중 / 신장 (제곱) 입니다")

weight=int(input("체중을 입력해주세요=> "))
print()
print("신장을 입력해주세요")
cm=float(input("키는 m단위로 적어주세요 =>"))
print()
bmi=weight/(cm*cm)
print(name+"님의 bmi지수는")
print(bmi)
print("이며,")

bmi=weight/(cm*cm)

if bmi < 18.5:
    print("저체중입니다.")
elif (18.5<= bmi <23):
    print("정상입니다.")
elif (23 <= bmi <25):
    print("과제중입니다.")
elif (25<= bmi < 30):
    print("비만입니다.")
else:
    print("고도비만입니다.")



print("기초대사량 구하기")
print()
a = int(input("몸무게를 적어주세요."))
b = int(input("키를 적어주세요."))
c = int(input("나이를 적어주세요."))
d = int(input("성별을 적어주세요. \n 여자=0 , 남자=1로 입력하세요 :"))

if (d == 0) :
    fmale = 665.1 + (9.56 * a) + (1.85 * b) - (4.68 * c)
    print(fmale)
else:
    print (66.47+(13.75*a)+(5*b)-(6.76*c))




print("활동 대사량을 구해봅시다.")
print()
rlch = input("기초대사량을 입력해주세요 = >")

print("활동이 적거나 운동을 안할 경우 = 1\n가벼운 활동 및 운동(1~3/주)을 하는 경우 = 2\n보통의 활동 및 운동(3~5일/주)을 하는 경우 = 3\n적극적인 활동 및 운동(6~7일/주)을 하는 경우 = 4\n매우 적극적인 활동 및 운동 선수인 경우 = 5")
ex = int(input("각 각의 맞는 숫자를 적어주세요 =>"))

if ex == 1 :
    aa = rlch * 0.2
    print(float((aa))
elif ex == 2:
    aa = rlch * 0.375
    print(float((aa))
elif ex == 3:
    aa = rlch * 0.555
    print(float((aa))
elif ex == 4:
    aa = rlch * 0.725
    print(float((aa))
else:
    aa = rlch * 0.9
    print(float((aa))
