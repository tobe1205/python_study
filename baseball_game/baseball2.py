
# import random
# number = random.randint(100,999) 
# print(number)

# i = number

# a = i // 100
# b = (i - (a * 100)) // 10
# c = (i % 10)

# while True : 
#     guess = int(input('숫자 3자리를 입력하세요: '))
#     if guess == i :
#         print('값은 %d, %d, %d' %(a,b,c) + ' strike! 정답입니다!')
#         break
#     elif i == ((guess == i // 100) == a or (guess == i - (a * 100)//10) == b or (guess == i % 10) == c):
#         print('one strike')
#         print('다시 숫자를 입력해주세요: ')


import random

def generate_numbers():
    # 지난 과제의 코드를 붙여 넣으세요.
    nums = []

    while len(nums) < 3:
        random_num = random.randint(0, 9)
        if random_num not in nums:
            nums.append(random_num)

    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return nums

def take_guess():
    # 지난 과제의 코드를 붙여 넣으세요.
    print("숫자 3개를 하나씩 차례대로 입력하세요.")

    guess_list = []
    while len(guess_list) < 3:
        guess = int(input(f"{len(guess_list) + 1}번째 숫자를 입력하세요: "))

        if guess < 0 or guess > 9:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
        elif guess in guess_list:
            print("중복된 숫자입니다. 다시 입력하세요.")
        else:
            guess_list.append(guess)

    return guess_list

def get_score(guess, answer):
    strike_count = 0
    ball_count = 0

    # 지난 과제의 코드를 붙여 넣으세요.
    for i in range(3):
        if guess[i] == answer[i]:
            strike_count += 1

    for i in range(3):
        if guess[i] in answer and guess[i] != answer[i]:
            ball_count += 1

    return f"{strike_count}S", f"{ball_count}B"

ANSWER = generate_numbers()
tries = 0

s = 0
b = 0

while True:
    user_guess = take_guess()
    s, b = get_score(user_guess, ANSWER)

    print(s, b)
    tries += 1

    if s == "3S":
        break

print(f"축하합니다. {tries}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.")
