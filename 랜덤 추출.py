import random
#하체 랜덤 리스트
leg = ['스쿼트', '점프스쿼트', '런지', '점프 런지' , '브릿지홀드' , '힙스쿼즈']
leg_one = random.choice(leg)
#상체 랜덤 리스트
arm = ['푸쉬업','벤치딥스','덤벨킥백','덤벨 사이드레터럴레이즈','덤벨 프론트레이즈','덤벨 숄더프레스']
arm_one = random.choice(arm)
#유산소 랜덤 리스트
hard = ['런닝머신', '싸이클', '천국의 계단','일립티컬머신','스텝퍼','로잉머신']
hard_one = random.choice(hard)
    
#원하는 부위 랜덤 추출

print("원하는 부위의 운동을 골라주세요. \n ex) 하체, 상체, 유산소, 스트레칭")
exercise = input()

if exercise == "하체" :
    print(leg_one + "을(를) 하세요.")
elif exercise == "상체" :
    print(arm_one + "을(를) 하세요.")
elif exercise == "유산소" :
    print(hard_one + "을 하세요.")
else:
    print("입력하신 부위의 운동은 없습니다.")

