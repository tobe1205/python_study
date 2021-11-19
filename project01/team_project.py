
cafelist = [
    {'제품명' : '아메리카노',
    '가격' : 5000
    },
    {'제품명' : '카페라떼',
    '가격' : 4500
    }
]

choice_list = []


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
    print('# 3. 장바구니')
    print('# 4. 메뉴 수정하기')
    print('# 5. 메뉴 삭제하기')
    print('# 6. 구매하기')
    print('# 7. 프로그램 종료하기')

# 2. 모든 메뉴 출력 함수
def all_menu():
    print('\n***** 카페 전체 메뉴 *****')
    print('=' * 30)
    print('{:^8s}    {:^12s}'.format('제품명', '가격',))
    print('=' * 30)
    
    for menu in cafelist: 
        print('{}    {:>8d}원'.format(menu['제품명'], menu['가격']))
    print('=' * 30)
    input()
    
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

# 3. 장바구니 보기 함수
def basket_look():
    print('\n   ***** 나의 장바구니 리스트 *****')
    print('=' * 50)
    print('{:^8s}{:^8s}{:^8s}{:^8s}{:^8s}'.format('제품명', '온도', '사이즈', '토핑','가격'))
    print('=' * 50)
    for choice in choice_list:
        print('{:^8s}{:^8s}{:^8s}{:^8s}{}'.format(choice['제품명'], choice['온도'], choice['사이즈'],choice['토핑']))
    print('=' * 50)



100
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
            menu['제품명'] = (input('- 수정할 이름({}): '.format(menu['제품명'])))
            menu['가격'] = int(input('- 수정할 가격({}): '.format(menu['가격'])))
        else:
            print('# 변경을 취소합니다.')
            input()
        print('수정이 완료되었습니다.')
        input()
    else:
        print('# 존재하지 않는 제품입니다.')
        input()
 

# 5. 메뉴 삭제
def delete_product():
    code = input_code('삭제')
    menu = get_product(code)

    if len(menu) > 0:
        cafelist.remove(menu)
        print('\n# 제품이 정상 삭제되었습니다.')
    else:
        print('# 존재하지 않는 제품입니다.')
    input()

# 6. 구매하기
def choice_menu():
    choice = {}

    print('\n메뉴 선택을 시작합니다!')

    choice['제품명'] = (input('[제품명] => '))
    x = input('[ 1. 아이스 | 2. 핫 ] => ')
    if x == '1':
        choice['온도'] = '아이스'
    elif x == '2':
        choice['온도'] = '핫'
    choice['사이즈'] = input('[ 1. 스몰 | 2. 라지 ] => ')
    if x == '1':
        choice['사이즈'] = '스몰'
    elif x == '2':
        choice['사이즈'] = '라지'
    choice['토핑'] = input('[ 1. 생크림 | 2. 샷추가 ] => ')
    if x == '1':
        choice['토핑'] = '생크림'
    elif x == '2':
        choice['토핑'] = '샷추가'

    choice_list.append(choice)
    print('[장바구니 저장완료!!')

# 7. 프로그램 종료 함수
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
        print(cafelist)
        print(choice_list)

        show_menu()
        select = (input('=> '))

        if select == '1':
            make_menu()
            print(cafelist)
        elif select == '2':
            all_menu()
        elif select == '3':
            basket_look()
        elif select == '4':
            modify_product()
        elif select == '5':
            delete_product()
        elif select == '6':
            choice_menu()
        elif select == '7':
            exit_program()
        else:
            print('# 메뉴를 잘못 입력했습니다.')

        input()

