
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

# 0~100까지의 정수 중 4의 배수를 가로로 출력(while문)