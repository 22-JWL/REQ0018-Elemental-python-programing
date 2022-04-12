nation=input("국가명을 입력하세요(한국, 미국, 스페인, 체코) :")

print()
print("== 번역 결과 ==")

if nation=='한국':
    print('영어 표기 : Korea')
    print(f'{nation} 수도 : Seoul')
elif nation=='미국':
    print('영어 표기 : USA')
    print(f'{nation} 수도 : Washington')
elif nation=='스페인':
    print('영어 표기 : Spain')
    print(f'{nation} 수도 : Madrid')
elif nation=='체코':
    print('영어 표기 : Czecho')
    print(f'{nation} 수도 : Prague')
else:
    print('아직 번역이 준비되지 않았습니다')

    



