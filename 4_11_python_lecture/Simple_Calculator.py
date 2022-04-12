a=int(input('정수1 입력: '))
b=int(input('정수2 입력: '))
op=input('연산자(+,-,*,/)중 입력:')

if not(op =='+' or op=='-' or op=='*' or op=='/'):
    print("알 수 없는 연산자 입니다")
else:
    if op=='+':
        #print(f'{a}+{b}={a+b}')
        result = a+b

    elif op =='-':
        result = a-b

    elif op =='*':
        result = a*b


    elif op =='/':
        result = a/b

# else: 안좋은 예
#     print('아직 준비되지 않았습니다 다음 학기에 시도해주세요 *^.^*')

print(f'{a} {op} {b}={result}')