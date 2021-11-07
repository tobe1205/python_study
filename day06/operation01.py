# 1. 문구 출력 v
#  -> 제목 
# 2. 난수 생성 v  
#  -> 랜덤 설정 v
# 3. 문제 출력 v
#  -> 문제 숫자 랜덤, Q. 숫자 하나씩 증가 v
#  -> 정답 입력 v
#  -> 맞으면 정답입니다. 아니면 틀렸어요~ 표시  v
#  -> 0을 입력시 게임을 종료  v
# 4. 게임이 종료되면 정답횟수, 틀린횟수 출력하기 v
#  -> 문제 맞출때 마다 정답횟수증가, 틀리면 틀린횟수 증가 설정 v
# 5. 더하기, 빼기, 곱하기 문제까지 출제 하기 
# 6. 난이도 상, 중, 하 설정하기!
#  -> 설정 제목, 난이도 범위 출력
#  -> 난이도 설정
#  -> 난이도 입력


import random

print('~~~~~~~~ 재미있는 사칙연산 게임 ~~~~~~~~')
print('[즐겁게 문제를 푸시다가 지겨우면 0을 누르세요~]')
print('=' * 30)

print('~~~~~~~~~~~~~~~~ 난이도를 설정합니다. ~~~~~~~~~~~~~~~~')
print('[ 1. 상 (1~100) | 2. 중 (1~50) | 3. 하 (1~20) ]')

while True :

    level = int(input('>> '))


    if level == 1:
        levelNum = 100
        print('난이도 상을 선택하셨습니다.')
        break
    elif level == 2:
        levelNum = 50
        print('난이도 중을 선택하셨습니다.')
        break
    elif level == 3:
        levelNum = 20
        print('난이도 하를 선택하셨습니다.')
        break
    else:
        print('잘못 입력하셨습니다. 다시 입력해주세요!')

ok = 0
no = 0
qNum = 1


while True:
    
    first = random.randint(1,levelNum)
    second = random.randint(1,levelNum)
    markNum = random.randint(1,3)
   

    if markNum == 1:
        mark = '+'
        real = first + second
    elif markNum == 2:
        if first == second:
            second -= 1
        mark = '-'
        real = first - second  
    else:
        mark = 'x'
        real = first * second
        
        
    print(f'Q{qNum}. {first} {mark} {second} = ??')
    qNum += 1

    answer = int(input('>> '))

  
    if answer == 0:
        print('게임을 종료합니다!')
        print('-' * 10)
        print(f'정답횟수 : {ok}회, 틀린횟수 {no}회')
        break
    
    if real == answer:
        print('정답입니다!!')
        ok +=1
    else:
        print('틀렸어요~')
        no +=1
