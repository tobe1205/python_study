
# 반복문, 탈출문 while문

# 회원 번호
user_num = 1 # 제어변수(begin) 반복문의 시작값

while user_num <= 10: # 조건식(end): 반복문의 끝값
    print(f'{user_num}번 회원님 안녕하세요!')
    user_num += 2 # 증감식(step): 종료시점을 결정
# 조건문을 잘못 만들게 되면 무한 루프가 되니 조심해야한다. 
# 무한루프 탈출 단축키 ctrl+C

# 1~10까지의 누적합
total = 0 # 총합을 누적저장할 변수
num = 1 # 1~10까지의 변경하면서 가질 변수

total += num
num += 1

while num <= 10:
    total += num
    num += 1

print('=' * 40)
print(f'총합: {total}')

print('='*40)

# 7~100까지의 정수 중 7의 배수들만 가로로 출력하기

num = 7 

while num <= 100:
    print(num, end=" ")
    num += 7

print() # 단순 줄개행

# 1~100까지의 정수 중 4의 배수를 가로로 출력
print('='*40)

num = 1

while num <= 100:
    if num % 4 == 0:
        print(num, end=" ")
    num += 1

print()

print('='*40)

# 1~100까지의 정수 중 6의 배수이면서 12의 배수가 아닌 수를 가로로 출력
num = 1

while num <= 100:
    if (num % 6 == 0) and (num % 12 != 0):
        print(num, end=" ")
    num += 1


# 1~9876사이의 정수 중 13의 배수의 갯수를 출력
print()
print('='*40)

num = 1
count = 0

while num <= 9876:
    if num % 13 == 0:
        count += 1
    num += 1
    
print(f'범위안의 13의 배수의 숫자 : {count}개')