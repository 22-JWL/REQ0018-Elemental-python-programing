a=(input("음료=>물, 커피, 탄산중 선택:"))
b=int(input("구입 갯수: "))
print("-- 주문 내용 --")
print("선택 음료: %s, 선택 갯수 : %d" %(a, b))

if a=='물':
    금액=b*600
elif a=='커피':
    금액=b*1200
elif a=="탄산":
    금액=b*900
else:
    금액=0
    print("물, 커피, 탄산중 선택해 주세요")
    
print("지불 금액 : %d" %금액)

