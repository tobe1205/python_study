
import random

print('~~~~~~~ 재미있는 사칙연산 게임 ~~~~~~~')
print('[즐겁게 문제를 푸시다가 지겨우면 0을 누르세요 ~')

print('~~~~~~~ 난이도를 설정합니다. ~~~~~~~~')
print('[1. 상 (1~100) | 2. 중 (1~50) | 3. 하 (1~20)]')

count = 0
count_down = 0
n = 0

level = int(input('>>> '))







while True :
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)    
    n += 1

    # print(secret1)
    # print(secret2)
    print(f'Q{n}. {num1} + {num2} = ??')
    guess =int(input('>> '))
    

    if guess == 0:
        print('게임을 종료합니다!')
        print('-'*40)
        print(f'정답횟수: {count}회, 틀린횟수: {count_down}회')
        break
    elif guess == (num1 + num2):
        count += 1
        print('정답입니다.')
    elif guess != (num1 + num2):
        count_down += 1
        print('틀렸어요~~')

    


    
    