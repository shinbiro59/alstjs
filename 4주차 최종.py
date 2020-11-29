#비만도 계산기

print("비만도 계산기")
print()
name=input("이름을 적어주세요")

weight=int(input("체중을 입력해주세요=> "))
print()
print("신장을 입력해주세요")
print("ex.155cm => 1.55 ")
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
print()

#기초대사량 구하기

print()
print("기초대사량 계산기")
print()
a = int(input("몸무게를 적어주세요."))
b = int(input("키를 적어주세요."))
c = int(input("나이를 적어주세요."))
d = int(input("성별을 적어주세요. \n 여자=0 , 남자=1로 입력하세요 :"))


print(name+"님의 기초대사량은")
if (d == 0) :
    fmale = 665.1 + (9.56 * a) + (1.85 * b) - (4.68 * c)
    print(fmale)
else:
    print (66.47+(13.75*a)+(5*b)-(6.76*c))
print("입니다.")
print()




#활동대사량 구하기
print()
print("활동 대사량 계산기")
print()

#rlch = 기초대사량
print("위의 결과 값인 소수점을 제거하고 입력해주세요")
rlch = float(input("기초대사량을 입력해주세요 = >"))
print("활동이 적거나 운동을 안할 경우 = 1\n가벼운 활동 및 운동(1~3/주)을 하는 경우 = 2\n보통의 활동 및 운동(3~5일/주)을 하는 경우 = 3\n적극적인 활동 및 운동(6~7일/주)을 하는 경우 = 4\n매우 적극적인 활동 및 운동 선수인 경우 = 5")
ex = int(input("본인의 활동량과 맞는 숫자를 적어주세요 =>"))
if ex == 1 :
    aa = rlch * 0.2
    print(aa)
elif ex == 2 :
    aa = rlch * 0.375
    print(aa)
elif ex == 3:
    aa = rlch * 0.555
    print(aa)
elif ex == 4:
    aa = rlch * 0.725
    print(aa)
else:
    aa = rlch * 0.9
    print(aa)


#식단 짜기
print("식단 짜기")
print("하루섭취량은 기초대사량+활동대사량보다는 적게 먹어야 살이 빠짐 \n *주의* 기초대사량만 기준으로 먹으면 안됨.\ n 기초대사량 : 숨만 쉬어도 소모되는 칼로리\n 홛동대사량 : 활동할 때 소모되는 칼로리")
print()

day = input("식단의 목적을 선택해주세요. \n 다이어트=0 , 벌크업=1로 입력하세요 :")

print(name+"님의 하루 식단은")

if (day == 0) :
    dietmeal = float(rlch) + float(aa)
    print(float(dietmeal)+"kcal 보다 적은 량을 섭취하세요")
else:
    dietmeal = float(rlch) + float(aa)
    print(float(dietmeal)+"kcal 보다 많은 량을 섭취하세요")
print()
print()


