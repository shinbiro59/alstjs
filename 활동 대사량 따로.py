print("활동 대사량을 구해봅시다.")
print()
rlch = input("기초대사량을 입력해주세요 =>")
print()
print("활동이 적거나 운동을 안할 경우 = 1 \n 가벼운 활동 및 운동 주 1-3회 = 2 \n 보통의 활동 및 운동 주 3-5회 = 3 \n 적극적인 활동 및 운동 주 6-7회 = 4 \n 매우 적극적인 활동 및 운동 선수 = 5")
print()

ex = int(input("각 각의 맞는 숫자를 적어주세요 =>"))
print()

if ex == 1 :
    aa = rlch * 0.2
    print(float(aa))
elif ex == 2 :
    aa = rlch * 0.375
    print(float(aa))
elif ex == 3:
    aa = rlch * 0.555
    print(float(aa))
elif ex == 4:
    aa = rlch * 0.555
    print(float(aa))    
else :
    aa = rlch * 0.9
    print(float(aa))
