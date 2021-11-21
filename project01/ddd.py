import sys
# 회원가입 리스트 타입
user = []

# 함수 정의부
# 메뉴를 출력하는 함수
def show_menu():
    print('\n 안녕하세요 ')
    print('#1 . 회원가입 ')
    print('#2 . 로그인 ')
    print('#3 . ID 찾기 ')
    print('#4 . 비밀번호 찾기 ')
    print('#5 . PW 바꾸기 ')
    print('#6 . 회원 탈퇴 ')
    print('#7 . 종료 ')

# 회원가입
def user_info():
    info = {}
    print('\n ☆ 회원 가입을 시작합니다. ☆')      
    info['이름'] = input('- 이름: ')
    info['별명'] = check_duplicate_code3()
    info['아이디'] = check_duplicate_code()
    if info['아이디'] not in user:
        print(' 사용가능 아이디 입니다')
    else:
        print('이미 등록된 아이디 입니다.')
    info['비밀번호'] = input('- 비밀번호: ')
    if info['비밀번호'] == input('- 비밀번호확인: '):
        print('비밀번호가 일치합니다')
    else:
        print('비밀번호가 일치하지 않습니다.')    
    user.append(info)
    print('회원가입 되셨습니다!')
    print('메뉴화면으로 돌아가시려면 Enter를 누르세요')
    input()
    return

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
            break
        elif (info['아이디'] != id) and (info['비밀번호'] == pw):
            print('아이디가 틀렸습니다.')
        elif (info['아이디'] == id) and (info['비밀번호'] != pw):
            print('비밀번호가 틀렸습니다.')

        input()

# 아이디 중복
def check_duplicate_code():    
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
            
# 별명 중복
def check_duplicate_code3():    
    while True:       
        info = input('- 별명: ')    
        flag = False  # 중복 플래그          
        # 중복 검증
        for p in user:
            if info == p['별명']:
                # 중복됨 
                print('중복되었습니다 다시 입력하세요')
                flag = True             
                break
        if flag == False:
            return info

def header_print1():
    print('\n\t\t*** 회원 아이디 조회 *** ')
    print('=' * 60)

def header_print2():
    print('\n\t\t\t*** 회원 비밀번호 조회 *** ')
    print('=' * 80)


# 별명를 입력받아 ~~~하는 함수
def input_code(msg):
    print(f'# {msg}하실 별명을 입력하세요.')
    code = input('별명: ')
    return code

def input_code2(msg):
    print(f'# {msg}하실 이름과 아이디를 입력하세요.')
    code = input('이름: ')
    return code

def input_code3(msg):
    print(f'# {msg}하실 아이디를 입력하세요.')
    code = input('아이디: ')
    return code

# 별명으로 해당 아이디을 찾아오는 함수
def get_info(code):
    for info in user:
        if code == info['별명']:
            return info
    return {} # 못 찾을 경우 상징적으로 빈 딕셔너리 리턴

# 이름 + 별명으로 비밀번호 찾아오는 함수
def get_info2(code):
    for info in user:
        if code == info['이름']:
            x = input('아이디: ')
            if info['아이디'] == x : 
                return info
    return {} # 못 찾을 경우 상징적으로 빈 딕셔너리 리턴


def get_info3(code):
    for info in user:
        if code == info['아이디']:
            return info
    return {} # 못 찾을 경우 상징적으로 빈 딕셔너리 리턴    

# 아이디 조회 처리 함수
def search_id():
    code = input_code('조회')
    info = get_info(code)

    if len(info) > 0:
        header_print1()
        print('[{:^7s}]님의 별명[{:^7s}], 아이디는 [{:^7s}]입니다.'.format(info['이름'], info['별명'], info['아이디']))
        print('=' * 60)
    else:
        print('# 존재하지 않는 아이디입니다.')

# 비밀번호 찾기 처리 함수    
def search_pw():
    code = input_code2('조회')
    info = get_info2(code)

    if len(info) > 0:
        header_print2()
        print('[{:^7s}]님의 별명[{:^7s}],아이디는 [{:^7s}], 비밀번호는 [{:^7s}] 입니다.'.format(info['이름'], info['별명'], info['아이디'], info['비밀번호']))
        print('=' * 80)
    else:
        print('# 존재하지 않는 비밀번호입니다.')


# 비밀번호 수정    
def modify_privercy():
    code = input_code3('수정')
    info = get_info3(code)

    if len(info) > 0:
        print('\n# [{}] {}님의 정보를 수정합니다.'.format(info['별명'], info['이름'] ))
        info['아이디']
        print('[ 1. 별명 변경 | 2. 비밀번호 변경 | 3. 취소 ]')
        select = int(input('>> '))
        
        
        if select == 1:
            info['별명'] = input('-수정할 별명({}): '.format(info['별명']))     
        elif select == 2:
            info['비밀번호'] = input('-수정할 비밀번호({}): '.format(info['비밀번호']))
        else:
            print('# 변경을 취소합니다.')
    else:
        print('#존재하지 않습니다.')    

# 제품 정보 삭제 처리 함수
def delete_user():
    code = input_code3('삭제')
    info = get_info3(code)
    if len(info) > 0:
        print('정말로 삭제하시겠습니까? [Y/N]')
        answer = input('>> ')
        if answer.lower() == 'y':
                user.remove(info)
                print('\n# 아이디가 정상 삭제 되었습니다.')
                print(user)
        else:
            print('삭제가 취소되었습니다.')     
    else:
        print('# 존재하지 않는 아이디입니다.')  

# 프로그램 종료처리 함수
def exit_program():
    import sys
    print("# 프로그램을 종료합니다. [Y/N]")
    answer = input('>> ')
    if answer.lower()[0] == 'y':
        sys.exit()
    else:
        return


# 실행부
if __name__ == '__main__':

    while True:
        show_menu()
        print(user)
        menu = int(input('메뉴 입력 = > '))
        if menu == 1:
            user_info()

        elif menu == 2:
            login()
            
        elif menu == 3:
            search_id()
        elif menu == 4:
            search_pw()
        elif menu == 5:
            modify_privercy()
        elif menu == 6:
            delete_user()
        elif menu == 7:
            exit_program()
