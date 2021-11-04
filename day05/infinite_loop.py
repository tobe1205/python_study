""""
# 무한 루프 break 사용
while True:
    num = int(input('숫자: '))

    if num == 0 : break
"""

money = 5000
# 각 제품을 몇개 샀는지에 대한 카운트 
cola = 0 
snack = 0
ice = 0

while True : # 무한루프 맞출때까지 계속 반복
    if money < 500 :
        print('구매를 종료합니다.')
        print(f'총 구매 목록 : 콜라 {cola}개, {snack}개, {ice}개')
        break
    elif money < 800 :
        print('[1.콜라: 500원]')
    elif money < 1000:
        print('[1.콜라: 500원 | 2. 과자: 1000원]')
    else:
        print('[1.콜라: 500원 | 2. 과자: 1000원 | 3. 아이스크림: 800원]')

    print(f'# 현재 잔액: {money}원')
    menu = int(input('> '))

    if menu == 1:
        print('콜라를 구매했습니다.')
        money -= 500
        cola += 1
    elif menu == 2:
        print('과자를 구매했습니다.')
        money -= 1000
        snack += 1
    elif menu == 3:
        print('아이스크림을 구매했습니다.')
        money -= 800
        ice += 1
    else:
        print('메뉴를 잘못 선택했습니다.')


