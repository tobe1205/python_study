import sys
# 회원가입 리스트 타입
user = []

print(user)
# 함수 정의부
# 메뉴를 출력하는 함수
def show_menu():
    print('\n 안녕하세요 ')
    print('#1 . 회원가입 ')
    print('#2 . 로그인 ')
    print('#3 . ID 찾기 ')
    print('#4 . PW 찾기 ')
    print('#5 . PW 바꾸기 ')
    print('#6 . 회원 탈퇴 ')
    print('#7 . 종료 ')

# 회원가입
def user_info():
    info = {}
    print('\n ☆ 회원 가입을 시작합니다. ☆')      
    info['이름'] = input('- 이름: ')
    info['아이디'] = input('- 아이디: ')
    if info['아이디'] in user:
        print(' 사용가능 아이디 입니다')
    else:
        print('이미 등록된 아이디 입니다.')
    info['비밀번호'] = input('- 비밀번호: ')
    if info['비밀번호'] == input('- 비밀번호확인: '):
        print('비밀번호가 일치합니다')
    else:
        print('비밀번호가 일치하지 않습니다.')
        return
    user.append(info)
    print('회원가입 되셨습니다!')
    print('메뉴화면으로 돌아가시려면 Enter를 누르세요')
    input()

# 로그인 함수
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
        

    
# in 키워드를 통해 key 값의 존재 여부를 체크할 수 있음


# 실행부
if __name__ == '__main__':
    while True: 
        show_menu()
        print(user)
        menu = int(input('메뉴 입력 = > '))
        if menu == 1:
            user_info()
        if menu == 2:
            login()
