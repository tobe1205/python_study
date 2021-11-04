
# 1~10까지의 총합 (while 문)

num = 1
total = 0 

while num <= 10:
    total += num
    num += 1
print(f'1~10까지의 합은 {total}')

# 1~10까지의 총합 (for문)

total = 0

for i in range(1,11):
    total += i
print(f'1~10까지의 합은 {total}')

# 7~100까지의 정수 중 7의 배수들만 가로로 출력하기(while문)

num = 7

while num <= 100:
    print(f'{num}', end= ' ')
    num += 7

# 7~100까지의 정수 중 7의 배수들만 가로로 출력하기(for문)

for i in range(7, 101,7):
    print(f'{i}', end= ' ')

print()
# 0~100까지의 정수 중 4의 배수를 가로로 출력(while문)

num = 0

while num <= 100:
    print(f'{num}', end=' ')
    num += 4

print()


num1 = 1

while num1 <= 100:
    if num1 % 4 == 0:
        print(num1, end=' ')
    num1 += 1

print()
# for문 변경

for num1 in range(0,101,4):
    print(f'{num1}',end =' ')

print()

# 1~100까지의 정수 중 6의 배수이면서 12의 배수가 아닌 수를 가로로 출력 (while문)
"""
x = 1

while x <= 100:
    if (x % 6 == 0) and (x % 12 != 0):
        print(f'{x}',end=' ')
    x += 1
"""

# for문으로 변경

for i in range(1,101):
    if (i % 6 == 0) and (i % 12 != 0):
        print(f'{i}',end=' ')

print()
# 1~9876사이의 정수 중 13의 배수의 갯수를 출력 (while문)

num = 1
count = 0

while num <= 9876:
    if num % 13 == 0:
        count += 1
    num += 1
print(f'13의 배수의 갯수는 : {count}개',end=' ')

print()
# for 문 변경
count1 = 0

for sum in range(1,100):
    if sum % 13 == 0:
        count1 +=1
print(f'13의 배수의 갯수는 : {count1}개',end=' ')

        