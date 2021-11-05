# 1. 예제와 같은 게임을 만들어 보자 v
# 2. 정답 기회 n번 남았다는 카운트를 만들자 v
# 3. 도전 기회 내에 성공하면 YOU WIN!!을, v
# 넘어서 성공하면 YOU WIN! 생략 or YOU LOSE! v
# 4. 몇번 도전에 성공했는지 마지막 안내만들기 
# 5. 1~ 해당입력한 정수까지의 범위를 같이 표현해서 나타내기
# 6. 혹시나 숫자를 입력하지 않았으면, 다시 입력하라는 문구 띄우기
# 7. 기회 모두 소진됐을 때, 계속 문제를 풀어주세요 문구 띄우기

# 랜덤 숫자 뽑기
# 입력 창 띄우기
# 
# 입력 받기 (while)
#   -> 숫자인지 아닌지 판단 (if)
#   정답인지 큰지 작은지
#       -> 정답일경우
#           =>  횟수 체크
#       -> 큰 경우
#           =>  max=입력
#       -> 작은경우
#           ->  min=입력

import random

rn = random.randint(1,100)
print(f'랜덤숫자: {rn}')

min = 1
max = 100

count = 10
countMax = 10 

print(f'[UP & DOWN 게임 - {min}~{max}사이의 숫자 중 어떤 숫자가 들어있을까요??')
print(f'도전기회: {countMax}번')
print('-' * 40)

while True:
    guess = int(input(f'숫자를 입력하세요 ({min}~{max}): '))
    
    count -=1

    if guess == rn : 
        break
    
    elif guess > rn :
        print('DOWN!!')
        if count >= 0: 
            print(f'정답 기회 {count}번 남음~~')
            print('-' * 40)
        elif count < 0:
            print(f'정답 기회 {-count}번 초과~~')
            print('-' * 40)
        max = guess
    elif guess < rn :
        print('UP!!')
        if count >= 0: 
            print(f'정답 기회 {count}번 남음~~')
            print('-' * 40)
        elif count < 0 :
            print(f'정답 기회 {-count}번 초과~~')
            print('-' * 40)
        min = guess
        
    if count == 0 :
        print('정답 기회 모두 소진! 계속 문제를 풀어주세요!')   
if count > 0 :
    print(f'정답입니다!! {(countMax-count)}번만에 맞추셨군요~')
    print('YOU WIN!')
            
elif count < 0 :
    print(f'정답입니다!! {(countMax-count)}번만에 맞추셨군요~')
    print('YOU LOSE!')