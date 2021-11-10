
namelist = []
phonelist = []

while True:

    print('\n-------연락처 관리 프로그램--------')
    print('1. 연락처 등록')
    print('2. 연락처 검색')
    print('3. 연락처 삭제')
    print('4. 연락처 수정')
    print('5. 모든 연락처 조회')
    print('6. 프로그램 종료')
    print('7. 프로그램 초기화')
    print('------------------------------------')

    menu = int(input('메뉴 입력: '))
    
    if menu == 1:
        print('연락처 등록을 시작합니다.')
        name = input('이름: ')
        phone = input('전화번호: ')
        namelist.append(name)
        phonelist.append(phone)
        print('{}님 연락처 저장 완료!'.format(name))
        print(namelist)
        print(phonelist)

    elif menu == 2:
        
        name = input('찾을 이름을 입력하세요: ')

        if name in namelist:
            idx = namelist.index(name)
            print(f'{namelist[idx]}님의 전화번호는 {phonelist[idx]}입니다.')

        else:
            print(f'{name}님은 연락처 목록에 없습니다.')
    
    elif menu == 3:
        
        name = input('삭제할 이름을 입력하세요: ')

        if name in namelist:
            idx = namelist.index(name)
            # namelist.remove(namelist[idx])
            # phonelist.remove(phonelist[idx])
            # namelist.remove(name)
            # phonelist.remove(phonelist[idx])
            del(namelist[idx])
            del(phonelist[idx])
            print(namelist)
            print(phonelist)
            
            print(f'{name}님의 정보가 정상적으로 삭제되었습니다.')

        else:
            print(f'{name}님은 연락처 목록에 없습니다.')
    
    elif menu == 4:
        
        name = input('수정할 연락처의 이름을 입력하세요: '  ) 
        
        if name in namelist:
            print(f'# {name}님의 연락처를 수정합니다.')
            idx = namelist.index(name)

            old_phone = phonelist[idx]
            phonelist[idx] = input('수정할 연락처를 입력하세요: ')
            print(f'{name}님의 전화번호가 {old_phone}에서 {phonelist[idx]}으로수정되었습니다.')
        else:
            print(f'{name}은 연락처에 없습니다.')
            
    elif menu == 5:
        if len(namelist) > 0:
            print('\n========전체 연락처 조회========')
        
            for idx in range(len(namelist)):
                print(f'# {idx+1}. {namelist[idx]} : {phonelist[idx]}')

        else:
            print('\n아직 등록된 데이터가 없습니다. 등록을 먼저 진행하세요!')
        # for name in namelist:
        #     idx = namelist.index(name)
            # print(f'# {idx+1}. {namelist[idx]} : {phonelist[idx]}')
    
    elif menu == 6:
        break

    elif menu == 7:
        print('모든 데이터가 삭제됩니다. 삭제하시겠습니까? [y/n]')
        answer = input('>> ')

        if answer.lower()[0] == 'y'or answer == 'ㅛ':
            namelist.clear()
            phonelist.clear()
            print('\n 모든 데이터가 초기화 되었습니다.')
        else:
            print('\n 초기화를 취소합니다.')
    
    else:
        print('메뉴를 잘못 입력했습니다.')




    
