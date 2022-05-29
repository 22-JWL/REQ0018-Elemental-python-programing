print("<<재욱이의 숫자 추출 연산>>")

integer = int(input("▣ 네자릿수 정수 =>"))

thou =integer/1000
hun = integer% 1000 / 100
ten = integer% 100 / 10
one = integer% 10
su = int(thou)+int(hun)+int(ten)+int(one)


print("===== 출력 결과 =====")
print("천의자리: %d" %thou)
print("백의자리: %d" %hun)
print("십의자리: %d" %ten)
print("일의자리: %d" %one)
print("%d+%d+%d+%d = %d" %(thou, hun, ten, one, int(su)))

input()