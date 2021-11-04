
for n in range(1,3):
    print(f'{n}번 회원님 안녕하세요!')


print('='*40)

# 횟수를 제어하기 쉽다.
for a in range(8):
    print('메롱~',end='')

print()
# 1부터 10까지의 총합
total = 0

for n in range(1,11):
    total += n
print('1~10까지의 총합은 {}입니다.'.format(total))


# 7~100까지의 정수 중 7의 배수들만 가로로 출력하기
for num in range(7,101,7):
    print(num, end=" ")

print()

# 0~100까지의 정수 중 4의 배수를 가로로 출력
for num in range(0,101,4):
    print(num, end=" ")

print()
# 1~100까지의 정수 중 6의 배수이면서 12의 배수가 아닌 수를 가로로 출력
num = 1

for num in range(1,101):
    if (num % 6 == 0) and (num % 12 != 0):
        print(num, end=" ")

print()
# 1~100까지의 정수 중 4의 배수를 가로로 출력
print('='*40)

num = 1

for num in range(1,100):
    if num % 4 == 0:
        print(num, end=" ")