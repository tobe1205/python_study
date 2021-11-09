

list = ['영웅재중', '최강창민', '유노윤호', '시아준수', '믹키유천']

while True: 
    print('삭제할 이름을 입력하세요!')
    name = input('> ')

    if name in list:
        list.remove(name)
        print('삭제후:', list)
        break
    else:
        print(f'{name}는(은) 없는 멤버입니다.')
        


