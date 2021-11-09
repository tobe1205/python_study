'''
list = ['영웅재중', '최강창민', '유노윤호', '시아준수', '믹키유천']
print('\n수정전:', list)

while True:

    modify = input('수정할 이름을 입력: ')

    if modify not in list:
        print('그런 멤버는 없어~~')
        continue
    else:
        change = input('새로운 이름: ')
        list[1] = change
        break
    
print('수정완료!')
print(f'수정후: {list}')
'''

# 정답
list = ['영웅재중', '최강창민', '유노윤호', '시아준수', '믹키유천']
while True:

    print('\n수정전:', list)
    old_name = input('수정할 이름을 입력: ')

    if old_name in list:
        new_name = input('새로운 이름: ')
        list[list.index(old_name)] = new_name
        print('수정완료!')
        print('\n수정후: ', list)
        break
    else:
        print('그런 멤버는 없어~~')
            

    
