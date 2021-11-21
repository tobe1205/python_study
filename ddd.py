import sys

cafelist = [
    {'제품명' : '아메리카노',
    '가격' : 5000
    },
    {'제품명' : '카페라떼',
    '가격' : 4500
    }
]

user = []

print(user)
# 함수 정의부

# 메뉴를 출력하는 함수
def login_menu():

    print('#1 . 회원가입 ')
    print('#2 . 로그인 ')
    
# 회원가입
def user_info():
    info = {}
    print('\n ☆ 회원 가입을 시작합니다. ☆')      
    info['이름'] = input('- 이름: ')
    info['아이디'] = check_duplicate_code2()
    if info['아이디']  not in user:
        print(' 사용가능 아이디 입니다')
    else:
        print('이미 등록된 아이디 입니다.')
    info['비밀번호'] = input('- 비밀번호: ')
    if info['비밀번호'] == input('- 비밀번호확인: '):
        print('비밀번호가 일치합니다')
    else:
        return
        print('비밀번호가 일치하지 않습니다.')
    user.append(info)
    print('회원가입 되셨습니다!')
    print('메뉴화면으로 돌아가시려면 Enter를 누르세요')
    input()


# 로그인
def login():
    print('----------로그인----------')
    print(user)
    for info in user:
        id = input('- 아이디: ')
        pw = input('- 비밀번호: ')
        if (info['아이디'] == id) and (info['비밀번호'] == pw):
            print('☆ 로그인 되셨습니다 ☆')
            print('{}님 환영합니다.'.format(info['이름']))
            return
        elif (info['아이디'] != id) and (info['비밀번호'] == pw):
            print('아이디가 틀렸습니다.')
        elif (info['아이디'] == id) and (info['비밀번호'] != pw):
            print('비밀번호가 틀렸습니다.')
        
        input()
        
# 중복
def check_duplicate_code2():    
    while True:       
        info = input('- 아이디: ')    
        flag = False  # 중복 플래그          
        # 중복 검증
        for p in user:
            if info == p['아이디']:
                # 중복됨 
                print('중복되었습니다 다시 입력하세요')
                flag = True             
                break
        if flag == False:
            return info

# 1. [로그인] 전체 메뉴         
def login_all():            
    while True: 
        login_menu()
        print(user)
        menu = int(input('메뉴 입력 = > '))
        if menu == 1:
            sign_up()
        if menu == 2:
            login()
                 
# 함수 정의부
# [관리자전용] head 함수
def show_manager():
    print('== 관리자 전용 ==')
    print('# 1. 메뉴 등록하기')
    print('# 2. 메뉴 수정하기')
    print('# 3. 메뉴 삭제하기')
    print('# 4. 취소')
    
# [관리자전용] 제품명 중복 확인 함수
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

# [관리자전용] 메뉴 등록 함수
def make_menu():
    menu = {}
    print('\n메뉴 등록을 시작합니다!')

    menu['제품명'] = check_duplicate_code()
    menu['가격'] = int(input('- 가격: '))

    cafelist.append(menu)
    print('메뉴 등록 완료!')

# [관리자전용] 메뉴 수정 처리 함수       
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

    else:
        print('# 존재하지 않는 제품입니다.')
 
# [관리자전용] 메뉴 삭제 함수
def delete_product():
    code = input_code('삭제')
    menu = get_product(code)

    if len(menu) > 0:
        cafelist.remove(menu)
        print('\n# 제품이 정상 삭제되었습니다.')
    else:
        print('# 존재하지 않는 제품입니다.')

# 3 .[매니저전용] 전체 함수
def manager_page():
    show_manager()
    select = int(input('=> '))

    if select == 1:
        make_menu()
    elif select == 2:
        modify_product()
    elif select == 3:
        delete_product()
    elif select == 4:
        print('취소합니다.')


# head 출력 함수
def show_menu():
    print('\n*** 안녕하세요! 카페입니다!! ***')
    print('# 1. 회원가입 | 로그인')
    print('# 2. 모든 메뉴보기')
    print('# 3. 관리자 전용')
    print('# 4. 프로그램 종료하기')

# 2. 모든 메뉴 출력 함수
def all_menu():
    print('\n***** 카페 전체 메뉴 *****')
    print('=' * 30)
    print('{:^8s}    {:^12s}'.format('제품명', '가격',))
    print('=' * 30)
    
    for menu in cafelist: 
        print('{}    {:>8d}원'.format(menu['제품명'], menu['가격']))
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


# 5. 프로그램 종료 함수
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

        show_menu()
        select = int(input('=> '))

        if select == 1:
            login_menu()
            menu = int(input('>> '))
            print(user)
            if menu == 1:
                user_info()
            elif menu == 2:
                login()
        elif select == 2:
            all_menu()
        elif select == 3:
            manager_page()         
        elif select == 4:
            exit_program()
        else:
            print('# 메뉴를 잘못 입력했습니다.')

        input()