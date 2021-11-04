# 1. 예제와 같은 게임을 만들어 보자 v
# 2. 정답 기회 n번 남았다는 카운트를 만들자 v
# 3. 도전 기회 내에 성공하면 YOU WIN!!을, v
# 넘어서 성공하면 YOU WIN! 생략 or YOU LOSE! v
# 4. 몇번 도전에 성공했는지 마지막 안내만들기 
# 5. 1~ 해당입력한 정수까지의 범위를 같이 표현해서 나타내기
# 6. 혹시나 숫자를 입력하지 않았으면, 다시 입력하라는 문구 띄우기
# 7. 기회 모두 소진됐을 때, 계속 문제를 풀어주세요 문구 띄우기


import random

rn = random.randint(1,100)
print(f'랜덤숫자: {rn}')

min = 1
max = 100

count = 10
count2 = 10 
print(f'도전기회: {count2}번')
print(f'[UP & DOWN 게임 - {min}~{max}사이의 숫자 중 어떤 숫자가 들어있을까요??')
print('-' * 40)


while True:
    
    guess = int(input(f'숫자를 입력하세요 ({min} ~ {max}): '))
    
    count -=1

    if guess == rn : 
        break
    
    elif guess > rn :
        print('DOWN!!')
        print(f'정답 기회 {count}번 남음~~')
        print('-' * 40)
        max = guess
    elif guess < rn :
        print('UP!!')
        print(f'정답 기회 {count}번 남음~~')
        print('-' * 40)
        min = guess    
    if count == 0 :
        print('정답 기회 모두 소진! 계속 문제를 풀어주세요!')   
if count > 0 :
    print(f'정답입니다!! {count2-count}번만에 맞추셨군요~')
    print('YOU WIN!')
            
elif count < 0 :
    print(f'정답입니다!! {count2-count}번만에 맞추셨군요~')
    print('YOU LOSE!')


# 질문 1. 기회 소진 되고나서 계속 틀리면 기회 -번 남음 문구가 나오는데 안보이게 가능한지
# 질문 2. 기회 횟수 0번째에 바로 "정답기회 모두 소진" 문구 어떻게 출력되게 하는지
