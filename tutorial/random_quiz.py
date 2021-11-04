# 1.예제와 같은 게임을 만들어 보자 v
# 2. 정답 기회 n번 남았다는 카운트를 만들자 v
# 3. 도전 기회 내에 성공하면 YOU WIN!!을, v
# 넘어서 성공하면 YOU WIN! 생략 or YOU LOSE! v
# 4. 몇번 도전에 성공했는지 마지막 안내만들기 
# 5. 1~ 해당입력한 정수까지의 범위를 같이 표현해서 나타내기
# 6. 혹시나 숫자를 입력하지 않았으면, 다시 입력하라는 문구 띄우기

import random

rn = random.randint(1,100)
print(f'랜덤숫자: {rn}')

count = 9

print('[UP & DOWN 게임 - 1~100사이의 숫자중 어떤 숫자가 들어있을까요???]')
print('도전기회: 10번')

while True:
    guess = (int(input('숫자를 입력하세요(1~100): ')))

    if (guess == rn) and (count >= 0):
        print(f'정답입니다!! --번만에 맞추셨군요')
        print('YOU WIN!')
        break
    elif guess <= rn:
        print('UP!!')
        print(f'정답 기회 {count}번 남음~~')
        count -= 1  
    elif guess >= rn:
        print('DOWN!!')
        print(f'정답 기회 {count}번 남음~~')
        count -= 1
    if (guess == rn) and (count < 0):
        print(f'정답입니다 --번만에 맞추셨군요')
        print('YOU LOSE..TRY AGAIN!!')




