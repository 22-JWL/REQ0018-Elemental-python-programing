a=5
type(a)
k=input('국어점수=')
e=input('영어점수=')
print(k+e)
type(k)
print(int(k)+int(e))
print("국어+영어=", (int(k)+int(e)))
print(f"꾹어+영어={(int(k)+int(e))}")
avg=(int(k)+int(e))/2
print(f"평균={avg}점")
print("평균=%.2f점" %avg)
print("평균%d점" %avg)
