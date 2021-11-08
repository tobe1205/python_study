
import sys

COLA = 1300
SPRITE = 1200
FANTA = 1000
POCARI = 1600

C_cnt = 0
S_cnt = 0
F_cnt = 0
P_cnt = 0

while True :

    print('# 앗!! 눈앞에 음료수 자판기가 나타났다!!')
    print('## 어떻게 할까??')
    print('# [ 1. 자판기 앞으로 간다 || 2. 지나친다 ]')

    choice = int(input('>> '))

    if choice == 1:
        print('# 음료수나 먹어볼까?? 지갑에 얼마가 있더라~~?')
        money = int(input('## 가진돈 입력 >> '))
        if money <= 0 : 
            print('\n## 나 거지였구나....집에 가자....')
            print('## GAME OVER~~')
            print(' [ 1. 다시하기 || 2. 종료하기 ]')
            choice = int(input('>> '))
            if choice == 1:
                print('\n' * 100)
                continue
            elif choice == 2:
                break
        elif money > 1000000:
            print('\n## 내가 이렇게 돈이 많을리 없어 이건 꿈이야!!!')
            print('## GAME OVER~~')
            print(' [ 1. 다시하기 || 2. 종료하기 ]')
            choice = int(input('>> '))
            if choice == 1:
                print('\n' * 100)
                continue
            elif choice == 2:
                sys.exit()
        else:
            print(f'\n$$ 현재 소유한 돈: {money}원')
        
        while True:
            print(f'## 음료수를 고르세요!! (현재 잔액: {money}원)')
            print('*** 1. {:<8s}: {:>5d}원'.format('코카콜라', COLA))
            print('*** 2. {:<8s}: {:>5d}원'.format('스프라이트', SPRITE))
            print('*** 3. {:<8s}: {:>5d}원'.format('환타오렌지', FANTA))
            print('*** 4. {:<8s}: {:>5d}원'.format('포카리스웨트', POCARI))
            print('*** 5. 집에가버리기~~~~')
            print('=' * 25)
            select = int(input('>> '))
            if select == 1:
                if money >= COLA:
                    money -= COLA
                    C_cnt += 1
                    print('# 코카콜라 득템~~')
                else :
                    print('## 돈이 부족해...')
            elif select == 2:
                if money >= SPRITE:
                    money -= SPRITE
                    S_cnt += 1
                    print('# 스프라이트 득템~~')
                else :
                    print('## 돈이 부족해...')
            elif select == 3:
                if money >= FANTA:
                    money -= FANTA
                    F_cnt += 1
                    print('# 환타오렌지 득템~~')
                else :
                    print('## 돈이 부족해...')
            elif select == 4:
                if money >= POCARI:
                    money -= POCARI
                    P_cnt += 1
                    print('# 포카리스웨트 득템~~')
                else :
                    print('## 돈이 부족해...')
            elif select == 5:
                print('\n==========뽑은 음료수 정보==========')
                print('*** {:<8s}: {:<5d}개'.format('코카콜라', C_cnt))
                print('*** {:<8s}: {:<5d}개'.format('스프라이트', S_cnt))
                print('*** {:<8s}: {:<5d}개'.format('환타오렌지', F_cnt))
                print('*** {:<8s}: {:<5d}개'.format('포카리스웨트', P_cnt))
                print(f'### 남은 돈 : {money}원')
                print('='* 30)
                print('~~~ 수 고 하 셨 습 니 다. ~~~')
                print('## 엔터를 눌러서 종료하세요 ##')
                sys.exit()
            else:
                print('# 아쉽게도 그런 음료는 없는 것 같다.')
            print('='* 30)
            print('## 현재 잔액: {}'.format(money))
            print('# [ 1. 추가 뽑기 || 2. 집에 가기 ]')
            select = int(input('>> '))
            if select == 1:
                print('\n' * 100)
                continue
            elif select == 2:
                print('\n==========뽑은 음료수 정보==========')
                print('*** {:<8s}: {:<5d}개'.format('코카콜라', C_cnt))
                print('*** {:<8s}: {:<5d}개'.format('스프라이트', S_cnt))
                print('*** {:<8s}: {:<5d}개'.format('환타오렌지', F_cnt))
                print('*** {:<8s}: {:<5d}개'.format('포카리스웨트', P_cnt))
                print(f'### 남은 돈 : {money}원')
                print('='* 30)
                print('~~~ 수 고 하 셨 습 니 다. ~~~')
                print('## 엔터를 눌러서 종료하세요 ##')
                sys.exit()
            else:
                print('\n' * 100)
                continue



        
    elif choice == 2:
        print('## GAME OVER~~')
        print(' [ 1. 다시하기 || 2. 종료하기 ]')
        choice = int(input('>> '))
        if choice == 1:
            print('\n' * 100)
        elif choice == 2:
            sys.exit()
    else :
        print('## 선택은 정확하게 하세요~~ \n 계속 진행하려면 엔터...')
        input()
        print('\n' * 100)
 