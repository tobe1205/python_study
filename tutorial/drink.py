import sys

cola = 1300
sprite = 1200
fanta = 1000
sweat = 1600

c_count = 0
s_count = 0
f_count = 0
s_count = 0

while True:
    print('# 앗!! 눈앞에 음료수 자판기가 나타났다!!')
    print('## 어떻게 할까??')
    print('# [ 1. 자판기 앞으로 간다 || 2. 지나친다 ]')
    choice = int(input('>> '))

    if choice == 1:
        print('# 음료수나 먹어볼까?? 지갑에 얼마가 있더라~~?')
        money = int(input('## 가진 돈 입력 >> '))
        if money == 0 :
            print('\n## 나 거지였구나.... 집에 가자....')
            print('## GAME OVER~~')
            print('# [ 1. 다시하기 || 2. 종료하기 ]')
            choice = int(input('>> '))
            if choice == 1:
                print('\n' * 100)
                continue
            elif choice == 2:
                sys.exit()
        elif money > 1000000 :
            print('## 내가 이렇게 돈이 많을리 없어 이건 꿈이야!!!')
            print('## GAME OVER~~')
            print('# [ 1. 다시하기 || 2. 종료하기 ]')
            choice = int(input('>> '))
            if choice == 1:
                print('\n' * 100)
                continue
            elif choice == 2:
                sys.exit()
        else :
            print('\n$$ 현재 소유한 돈: {}원'.format(money))
        
        while True : 
            print(f'## 음료수를 고르세요!! (현재 잔액: {money}원)')
            print(f'*** 1. 코카콜라     :  {cola}원')
            print(f'*** 2. 스프라이트    :  {sprite}원')
            print(f'*** 3. 환타오렌지    :  {fanta}원')
            print(f'*** 4. 포카리스웨트     :  {sweat}원')
            print(f'*** 5. 집에 가버리기~~~~')
            print('=' * 30)
            select = int(input('>> '))

            if select == 1:
                if money >= cola:
                    money -= cola
                    c_count += 1
                    print('#코카콜라 특템 ~~')
                else:
                    print('## 돈이 부족해...')
            elif select == 2:
                if money >= sprite:
                    money -= sprite
                    s_count += 1
                    print('#스프라이트 특템 ~~')
                else:
                    print('## 돈이 부족해...')
            elif select == 3:
                if money >= fanta:
                    money -= fanta
                    f_count += 1
                    print('#환타오렌지 특템 ~~')
                else:
                    print('## 돈이 부족해...')
            elif select == 4:
                if money >= sweat:
                    money -= sweat
                    s_count += 1
                    print('#포카리스웨트 특템 ~~')
                else:
                    print('## 돈이 부족해...')
            elif select == 5:
                print('\n ========== 뽑은 음료수 정보 ==========')
                print('*** {:<8s}{:3d}개'.format('코카콜라',c_count))
                print('*** {:<8s}{:3d}개'.format('스프라이트',s_count))
                print('*** {:<8s}{:3d}개'.format('환타오렌지',f_count))
                print('*** {:<8s}{:3d}개'.format('포카리스웨트',s_count))
                print("### 남은 돈: {}원".format(money))
                print("=====================================")
                print("~~~ 수 고 하 셨 습 니 다. ~~~")
                input("## 엔터를 눌러서 종료하세요 ##")
                sys.exit()
            else:
                print('# 아쉽게도 그런 음료는 없는 것 같다.')
            
            print('='* 40 )
            print('## 현재 잔액: {}원'.format(money))
            print('# [ 1. 추가 뽑기 || 2. 집에 가기]')
            select = int(input('>> '))
            if select == 1:
                print('\n' *100)
                continue
            elif select == 2:
                print('\n ========== 뽑은 음료수 정보 ==========')
                print('*** {:<8s}{:3d}'.format('코카콜라',c_count))
                print('*** {:<8s}{:3d}'.format('스프라이트',s_count))
                print('*** {:<8s}{:3d}'.format('환타오렌지',f_count))
                print('*** {:<8s}{:3d}'.format('포카리스웨트',s_count))
                print("### 남은 돈: {}원".format(money))
                print("=====================================")
                print("~~~ 수 고 하 셨 습 니 다. ~~~")
                input("## 엔터를 눌러서 종료하세요 ##")
                sys.exit()
            else :
                print('\n' * 100)
                continue
    elif choice == 2:
        print('## GAME OVER~~')
        print('# [ 1. 다시하기 || 2. 종료하기 ]')
        choice = int(input('>> '))
        if choice == 1:
            print('\n' * 100)
            continue
        elif choice == 2:
            sys.exit()
    else:
        print('## 선택은 정확하게 하세요~~\n # 계속 진행하려면 엔터...')
        input()
        print('\n' * 100)












    