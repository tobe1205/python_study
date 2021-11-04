 # 구구단 만들기 다시 도전!
 # 1. while 문으로 2단 만들기
 # 2. for 문으로 변경
 # 3. 입력하는 정수가 단이 되는 구구단으로 변경 
 # 4. 다시 while문으로 변경 
 # 5. 반복 연습
"""
print('='*40)

level = int(input("구구단 단수: "))

for n in range(1,10):
    print(f'{level} x {n} = {level*n}')

print('='*40)
"""




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






 