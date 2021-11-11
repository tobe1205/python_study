
import sys

menulist = {}
print(menulist)

while True: 

    print('\n====== 음식점 메뉴 관리 프로그램 ======')
    print('# 1. 신규 메뉴 등록하기')
    print('# 2. 메뉴판 전체보기')
    print('# 3. 프로그램 종료하기')
    print('=====================================')

    select = (input('# 메뉴 입력: '))

    if select == '1':
        menu = input('메뉴명: ')

        if menu not in menulist:
            price = (input('가격: '))
            menulist[menu] = price
            print(f'신규 메뉴 {menu}(이)가 등록되었습니다.')
            print(menulist)
        else: 
            print(f'{menu}(은)는 이미 등록된 메뉴입니다.')

    elif select == '2':
        print('=======메뉴판=======')
        for food in menulist:
            print(f'{food} : {menulist[food]}원')
        print('=====================')
        print(' 1. 수정 | 2. 삭제 | 3. 나가기')
        choice = input('=> ')
        if choice == '1':
            print('가격을 변경할 메뉴의 이름을 입력하세요.')
            menu = input('=> ')
            if menu in menulist:
                new_price = input('변경할 가격: ')
                menulist[menu] = new_price
                print(f'{menu}의 가격이 {new_price}원으로 변경되었습니다.')
            
            else: 
                print(f'{menu}(은)는 등록된 메뉴가 아닙니다.')
        elif choice == '2':
            print('삭제할 메뉴명을 입력하세요.')
            menu = input('=> ')
            if menu in menulist:
                del(menulist[menu])
                print(f'{menu}이(가) 삭제되었습니다.')

            else:
                print(f'{menu}(은)는 등록된 메뉴가 아닙니다.')

    elif select == '3':
        print('# 프로그램을 종료하시겠습니까 [Y/N]')
        choice = input('=> ')

        if choice.lower() =='y':
            print('프로그램을 종료합니다.')
            sys.exit()
        else:
            print('종료를 취소합니다.')
            continue
    else:
        print('메뉴를 잘못 입력했습니다.')

    input('\n메뉴를 보시려면 Enter를 입력하세요..')


# print("*** {:<8s}: {:3d}개".format("코카콜라", C_cnt))
