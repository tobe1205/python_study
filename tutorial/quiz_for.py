
# 1~10까지의 총합

total = 0 

for num in range(1,11):
    total += num
print(f'1~10까지의 합은 {total}')

# 7~100까지의 정수 중 7의 배수들만 가로로 출력하기

for a in range(7,101,7):
    print(a, end= ' ')

print()

# 0~100까지의 정수 중 4의 배수를 가로로 출력

for b in range(0,101,4):
    print(f'{b}', end=' ')


print()


for num1 in range(1,101):
    if num1 % 4 == 0:
        print(num1, end=' ')

print()

# 1~100까지의 정수 중 6의 배수이면서 12의 배수가 아닌 수를 가로로 출력

x = 1

for x in range(1,101):
    if (x % 6 == 0) and (x % 12 != 0):
        print(f'{x}',end=' ')

print()

# 1~9876사이의 정수 중 13의 배수의 갯수를 출력

count = 0

for num in range(1,9877):
    if num % 13 == 0:
        count += 1

print(f'13의 배수의 갯수는 : {count}개',end=' ')
