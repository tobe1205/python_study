cafelist = [
    {'제품명' : '아메리카노',
    '가격' : 5000
    },
    {'제품명' : '카페라떼',
    '가격' : 4500
    }
]
print(cafelist)

# 함수 정의부

# 제품명 중복 확인 함수
def check_duplicate_code():    
    while True:       
        name = input('- 제품명: ')    
        flag = False  # 중복 플래그          
        # 중복 검증
        for p in cafelist:
            if name == p['제품명']:
                # 중복됨
                print('# 제품 이름이 중복되었습니다. 다시 입력하세요!')   
                flag = True             
                break
        if flag == False:
            return name

# 1. 메뉴 등록 함수
def make_menu():
    menu = {}
    print('\n메뉴 등록을 시작합니다!')

    menu['제품명'] = check_duplicate_code()
    menu['가격'] = int(input('- 가격: '))

    cafelist.append(menu)
    print('메뉴 등록 완료!')

# head 출력 함수
def show_menu():
    print('\n*** 안녕하세요! 카페입니다!! ***')
    print('# 1. 메뉴 등록하기')
    print('# 2. 모든 메뉴 조회')
    print('# 3. 개별 메뉴 정보 조회')
    print('# 4. 메뉴 수정하기')
    print('# 5. 메뉴 정보 삭제하기')
    print('# 6. 프로그램 종료하기')

# 2. 모든 메뉴 출력 함수
def all_menu():
    print('\n***** 카페 전체 메뉴 *****')
    print('=' * 30)
    print('{:^8s}    {:^12s}'.format('제품명', '가격',))
    print('=' * 30)
    for menu in cafelist: 
        print('{}    {:>10d}원'.format(menu['제품명'], menu['가격']))
    print('=' * 30)  

# 제품코드를 입력받는 함수
def input_code(msg):
    print(f'# {msg}하실 제품의 이름을 입력하세요')
    name = input('>> ')
    return name

# 제품번호로 해당 제품을 찾아오는 함수
def get_product(name):
    for menu in cafelist:
        if name == menu['제품명']:
            return menu
    return {} # 못 찾을 경우 상징적으로 빈 딕셔너리 리턴

# 3. 개별 메뉴 조회 처리 함수
def search_product():
    name = input_code('조회')
    menu = get_product(name)

    if len(menu) > 0:
        print('{}\t\t{}원'.format(menu['제품명'], menu['가격']))
    else:
        print('# 존재하지 않는 제품입니다.')

 # 4. 메뉴 수정 처리 함수       
def modify_product():
    name = input_code('수정')
    menu = get_product(name)

    if len(menu) > 0:
        print('\n# {}의 정보를 수정합니다.'.format(menu['제품명']))

        print('[ 1. 이름 변경 | 2. 단가 변경 | 3. 일괄 변경 | 4. 취소 ]')
        select = int(input('>> '))

        if select == 1:
            # 딕셔너리 수정: 딕셔너리변수[key] = new_value
            menu['제품명'] = input('- 수정할 이름({}): '.format(menu['제품명']))
        elif select == 2:
            menu['가격'] = int(input('- 수정할 가격({}): '.format(menu['가격'])))
        elif select == 3:
            menu['제품명'] = (input('- 수정할 수량({}): '.format(menu['제품명'])))
            menu['가격'] = int(input('- 수정할 가격({}): '.format(menu['가격'])))
        else:
            print('# 변경을 취소합니다.')

    else:
        print('# 존재하지 않는 제품입니다.')
 

# 5. 메뉴 삭제

# 6. 프로그램 종료 함수
def exit_program():
    import sys
    print('\n# 프로그램을 종료합니다. [Y/N]')
    answer = input('>> ')
    if answer.lower() == 'y':
        sys.exit()
    else:
        return

if __name__ == '__main__':
    
    while True:

        show_menu()
        select = int(input('=> '))

        if select == 1:
            make_menu()
            print(cafelist)
        elif select == 2:
            all_menu()
        elif select == 3:
            search_product()
        elif select == 4:
            modify_product()
        elif select == 5:
            pass
        elif select == 6:
            exit_program()