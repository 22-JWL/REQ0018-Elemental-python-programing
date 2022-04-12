age= int(input("현재 당신은 몇살입니까? :"))
if age < 14:
    print("당신은 초글링입니다.")
elif age < 17:
    print("당신은 중딩입니다.")
elif age < 20:
    print("당신은 고딩입니다.")
elif age < 25:
    print("당신은 학식입니다.")
else:
    print("당신은 사회인입니다! 빨리 일 하십시오!")
print("내년에는", age +1, "살이 되는 군요!")