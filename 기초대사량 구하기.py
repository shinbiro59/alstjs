print("기초대사량 구하기")
print()
a = int(input("몸무게를 적어주세요. : "))
b = int(input("키를 적어주세요. : "))
c = int(input("나이를 적어주세요. : "))
d = int(input("성병을 적어주세요. \n 여자=0 , 남자=1로 입력하세요 :"))


if (d == 0) :
    fmale = 665.1 + (9.56 * a) + (1.85 * b) - (4.68 * c)
    print(fmale)
else : 
    print (66.47 + (13.75 * a) + (5 * b) - (6.76 * c))


