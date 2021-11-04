 # 구구단 만들기 다시 도전! 
 # 1. while 문으로 2단 만들기 v 
 # 2. for 문으로 변경 - for문 while문 변경 시 어떤 것들이 변하는지 잘 확인할 것
 # 3. 입력하는 정수가 단이 되는 구구단으로 변경 v
 # 4. 다시 while문으로 변경 v
 # 5. 중첩 반복문으로 2~9단까지 출력 v
 # 5. 반복 연습


for a in range(2,10):
    print(f'구구단 {a}단')
    for b in range(1,10):
        print(f'{a} x {b} = {a * b}')


"""
print('='*40)

level = int(input("구구단 단수: "))

for n in range(1,10):
    print(f'{level} x {n} = {level*n}')

print('='*40)



# level = int(input('구구단 단수: '))
# print(f'구구단 {level}')
 
# a = 1

# while a <= 9:
#     print(f'{level} x {a} = {level * a}')
#     a += 1



# 중첩 반복문 

for level in range(2,10):
    print(f'구구단 {level}단')
    for line in range(1,10):
        print(f'{level} x {line} = {level * line}')
    print('='* 40)
"""



 