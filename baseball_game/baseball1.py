import random
#1
a = random.randrange(0, 10)
while True:
    b = random.randrange(0, 10)
    if(a!=b):
        break
while True:
    c = random.randrange(0, 10)
    if(a!=c and b!=c):

        break


count = 0

#2
while True:


    num1 = int(input("첫번째 숫자:"))

    num2 = int(input("두번째 숫자:"))

    while num1 == num2:

        print("중복된 숫자. 다시입력")

        num2 = int(input("두번째 숫자:"))

    num3 = int(input("세번째 숫자:"))

    while num3 == num1 or num3 == num2:

        print("중복된 숫자. 다시입력")

        num3 = int(input("세번째 숫자:"))
        
    strike = 0
    ball = 0
    count += 1
    if a==num1:
        strike += 1
    if b==num2:
        strike += 1
    if c==num3:
        strike += 1
    if a == num2 or a==num3:
        ball += 1
    if b == num1 or b==num3:
        ball += 1
    if c == num2 or c==num1:
        ball += 1
    print(count,"번째 도전")
    print("Strike:",strike,"Ball:",ball)
    if strike == 3:
        break
print(count,"회 만에 성공하셨습니다!")