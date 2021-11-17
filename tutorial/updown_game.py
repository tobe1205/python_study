
import random

secret = random.randint(1,100)
print(secret)
print(' [UP & DOWN 게임 - 1~100사이의 숫자 중 어떤 숫자가 들어있을까요???]')
print('-' * 40)

min = 1
max = 100
count  = 0
count_down = 10


print('# 게임의 난이도를 설정해주세요!')
print('[1. 상 | 2. 중 | 3. 하]')

level = (int(input('>>> ')))

if level == 1:
    print('난이도 상을 선택했습니다. 기회가 4번 주어집니다.')
    count_down = 4
elif level == 2:
    print('난이도 중을 선택했습니다. 기회가 6번 주어집니다.')
    count_down = 6
elif level == 3:
    print('난이도 하을 선택했습니다. 기회가 8번 주어집니다.')
    count_down = 8
else :
    print('난이도 선택이 잘못되었음으로, 상난이도로 자동 시작됩니다.')
    count_down = 4

while True :

    if count_down == 0  :
        print('정답 기회 모두 소진! 계속 문제를 풀어주세요!')

    if count_down > 0:
        answer = int(input(f'\n# 숫자를 입력하세요({min} ~ {max} | {count_down}): ')) 
    else:
        answer = int(input(f'\n# 숫자를 입력하세요({min} ~ {max}): '))   

    if (min > answer) or (max < answer):
        print('\n# 범위를 벗어난 값을 입력했습니다.')
        continue


    count += 1
    count_down -= 1

    if secret == answer :
        print(f'정답입니다!! {count}번만에 맞추셨군요~')
        if count_down >= 0:
            print('YOU WIN!')
        else:
            print('YOU LOSE!')
        break
    
    elif secret > answer :
        print('UP!!')
        min = answer
    else:
        print('DOWN!!')
        max = answer
