import random

while True:
    n=random.randint(-1, 100)
    if n==-1:
    print(f"n={n}")
    break
elif n%2==0 :
    print(f"{n}는 짝수입니다")
else:
    print(f"{n}는 홀수입니다")