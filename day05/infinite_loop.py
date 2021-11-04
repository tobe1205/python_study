""""
# 무한 루프 break 사용
while True:
    num = int(input('숫자: '))

    if num == 0 : break
"""

money = 5000

cola = 0
snack = 0
ice = 0

while True:

    if money < 1000:
        print('[1. 콜라: 500원 | 3. 아이스크림 800원]')
    
    elif money < 800:
        print('[1. 콜라 500원]')
        
    elif money < 500:
        print('구매를 종료합니다.')
        print(f'총 구매 목록: 콜라 {cola}개, 과자 {snack}개, 아이스크림 {ice}')
        break
    else:
        print('[1. 콜라: 500원 | 2. 과자: 1000원 | 3. 아이스크림 800원]')
