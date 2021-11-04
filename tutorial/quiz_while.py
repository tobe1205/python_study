# 1~100까지 홀수값을 가로로 (while)
a = 1

while a <= 100:
    print(f'{a}', end = ' ')
    a += 2

print()

# 0~100까지 짝수값을 가로로
b = 0
while b < 101:
    print(f'{b}',end=' ')
    b +=2

print()

# 1~10까지의 총합 (while 문)
c = 1
total = 0 

while c <= 10:
    total += c
    c += 1
print(f'1~10까지의 총합: {total}')

print()

# 7~100까지의 정수 중 7의 배수들만 가로로 출력하기(while문)
a = 7

while a <= 100:
    print(f'{a}', end = ' ')
    a += 7

print()

# 0~100까지의 정수 중 4의 배수를 가로로 출력(while문)
d = 0

while d <= 100: 
    print(f'{d}', end = ' ')
    d += 4

print()

# 1~100까지의 정수 중 6의 배수이면서 12의 배수가 아닌 수를 가로로 출력 (while문)
f = 1

while f <= 100:
    if (f % 6 == 0) and (f % 12 != 0):
        print(f'{f}',end=' ')
    f += 1

print()

# 1~9876사이의 정수 중 13의 배수의 갯수를 출력 (while문)
e = 1
count = 0

while e <= 9876:
    if e % 13 == 0:
        count += 1
    e += 1
print(f'13의 배수: {count}개')
    

