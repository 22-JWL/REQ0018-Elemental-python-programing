num = 3
sort ="coffee"
print("나는 오늘 %d잔의 %s를 마셨다."%(num, sort))
name = "홍길동"
age = 20
print(f"나의 이름은 {name}입니다. 나이는 {age}살 입니다.")
print(f"10년 후에 {age+10}살이 됩니다.")
print("동물 =>", end =" ")
print("강아지 ", end=", ")
print("고양이")


name=input("이름을 입력하세요=> ")

print(f"입력된 이름: {name}")

name=input("이름을 입력하세요=> ")#변수 초기화

order = input("==> 어떤 음료를 주문하시겠어요?")
number = float(input("==> 몇 잔 드릴까요?"))
print()
print("==> %s님은 %s를 %f잔 주문하셨습니다."%(name, order, number))
print(f"==> {name}님은 {order}를 {number}잔 주문하셨습니다")

