# 전역변수 정의부
inventory = []

# 함수 정의부

# 1 제품번호의 중복을 확인하는 함수
def check_duplicate_code():
    while True:
        code = input('- 제품 번호: ')
        flag = False # 중복 플래그
        # 중복 검증
        for p in inventory:
            if code == p['제품번호']:
                # 중복됨
                print('# 제품 번호가 중복되었습니다. 다시 입력하세요!')
                flag = True
                break
        if flag == False:
            return code


# 1-1 제품등록을 수행하는 함수
def insert_product():
    product = {}
    print('\n# 제품 정보 등록을 시작합니다.')
    
    product['제품번호'] = check_duplicate_code()
    product['제품명'] = input('- 제품명: ')
    product['가격'] = int(input('- 가격: '))
    product['수량'] = int(input('- 수량: '))
    product['총액'] = product['가격'] * product['수량']

    inventory.append(product)
    print('\n# 제품 등록이 정상 처리되었습니다.')
    print('\n# 메뉴화면으로 돌아가시려면 Enter를 누르세요.')
    input()

# 2. 모든 제품정보 조회하는 함수
def all_arrange_product():
    total = 0
    print('\n            *** 창고 재고 정보 ***')
    print('=' * 50)  
    print('제품번호     제품명      수량        단가        총액')
    print('=' * 50)  
    for p in inventory:
        total += p['총액']
        print(f"{p['제품번호']}           {p['제품명']}         {p['수량']}개      {p['가격']}원     {p['총액']}원")  
    print('=' * 50)
    print(f'                         창고 전체 제품 총액: {total}원')
    print('\n# 메뉴화면으로 돌아가시려면 Enter를 누르세요.')
    input()
    
    
# 3. 개별 제품정보 조회하는 함수
def arrange_product():
    print('# 조회하실 제품의 번호를 입력하세요.')
    code = input('-제품번호: ')
    for i in inventory:
        if code == i['제품번호']:
            print('\n            *** [{}] {} 재고 정보 ***'.format(code, i['제품명']))
            print('=' * 50)
            print('제품번호     제품명      수량        단가        총액')
            print('=' * 50)
            print(f"{i['제품번호']}           {i['제품명']}         {i['수량']}개      {i['가격']}원     {i['총액']}원")
            print('=' * 50)
        
            # print('[{}] 제품코드에 해당하는 제품 정보가 등록되지 않았습니다.'.format(code))    
    print('\n# 메뉴화면으로 돌아가시려면 Enter를 누르세요.')
    input()    

# 4. 제품정보 수정하는 함수 
def modify_product():
    print('# 수정하실 제품의 번호를 입력하세요')
    code = input('-제품번호: ')
    for x in inventory:
        if code == x['제품번호']:
            print('# [{}] {} 제품의 정보를 수정합니다.'.format(code, x['제품명']))
            print('[ 1. 수량 변경 | 2. 단가 변경 | 3. 일괄 변경 | 4. 취소 ]')
            choice = int(input('=>'))
            if choice == 1:
                new_amount = int(input('수정할 수량: '))
                x['수량'] = new_amount
            elif choice == 2:
                new_price = int(input('수정할 가격: '))
                x['가격'] = new_price
            elif choice == 3:
                new_amount = int(input('수정할 수량: '))
                x['수량'] = new_amount
                new_price = int(input('수정할 가격: '))
                x['가격'] = new_price
            x['총액'] = x['수량'] * x['가격']
            print(' {}의 정보수정이 정상 처리되었습니다.'.format(code))
            
            if choice == 4:
                print('#변경을 취소합니다.')
                print('[{}] 제품코드에 해당하는 제품 정보가 등록되지 않았습니다.'.format(code))
                print('\n# 메뉴화면으로 돌아가시려면 Enter를 누르세요.')
                input()  
            

    
# 5. 입력된 제품 정보 삭제하는 함수 -에러...
def delete_product():
    print('삭제하실 제품의 번호를 입력하세요.')
    code = input('-제품번호: ')
    for n in inventory:
        if code == n['제품번호']:
            print('[{}] {} 제품의 정보를 삭제합니다.'.format(code, n['제품명']))
            print('\n{}의 정보삭제가 정상 처리되었습니다.'.format(n['제품명']))
            del(n)


if __name__ == '__main__':
    
    while True:
        print(inventory)

        print('*** 재고 관리 프로그램 ***')
        print('# 1. 제품 정보 등록하기')
        print('# 2. 모든 제품정보 조회')
        print('# 3. 개별 제품정보 조회')
        print('# 4. 제품정보 수정하기')
        print('# 5. 제품정보 삭제하기')
        print('# 6. 프로그램 종료하기')

        menu = input('# 메뉴 입력: ')
        
        if not menu.isdecimal():
            print('숫자를 입력하세요.')
            continue
        else:
            menu = int(menu)

        if menu < 1 or menu > 6:
            print('입력 범위가 알맞지 않습니다.(1 ~ 6)입력')

        if menu == 1:
            insert_product()
        elif menu == 2:
            all_arrange_product()
        elif menu == 3:
            arrange_product()
        elif menu == 4:
            modify_product()
        elif menu == 5:
            delete_product()
        elif menu == 6:
            print('#프로그램을 종료합니다. [Y/N]')
            choice = input('=>')
            if choice.lower() == "y":
                print("프로그램을 종료합니다.")
                break
            else:
                continue
        


        
 
                

            
            
            
            