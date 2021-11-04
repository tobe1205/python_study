# 3자리 숫자 맞추기 

import random
number = random.randint(1,999) 
print(number)

while True :
    guess = int(input('숫자를 입력하세요: '))
    if guess == number :
        print('정답입니다.')
        break 
    elif guess > number:
        print('더 작은 수 입니다.')
    else:
        print('더 큰 수 입니다.')