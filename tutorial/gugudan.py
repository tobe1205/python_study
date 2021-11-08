# 2단 만들기
#  입력한 값을 단수로
# for문으로
# 중첩 for문으로 2~9단까지 출력


# n = 1
# level = int(input('구구단 단수: '))
# print(f'구구단 단수: {level}단')

# while n <= 9:
#     print(f'{level} x {n} = {level * n}')
#     n += 1

# for n in range(1,10):
#     print(f'{level} x {n} = {level * n}')

for level in range(2,10):
    for n in range(1,10):
        print(f'{level} x {n} = {level * n}')