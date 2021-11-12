# 플레이어의 이름을 저장할 리스트
player_list = []
number_list = ['0']
print('### 베스킨라빈스~~~ㅆㅓ리 원~!')
print('- 참여인원을 입력(최소2 최대 4)')

while True:

    player_num = int(input('>>> '))

    if player_num < 2 or player_num > 4:
        print('# 인원 범위가 알맞지 않음(2 ~ 4 입력)')
        continue
    elif player_num

    # 인원은 제대로 적음
    print(f'\n{player_num}명의 플레이어가 참여했습니다!')
    print('## 플레이어의 닉네임을 등록합니다.')
    
    for i in range(player_num):
        while True:
            player_name = input(f'# {i+1}번 플레이어 이름: ')
            
            # 이름 검증
            # 1. 이름을 안적은 경우
            if len(player_name.strip()) == 0:
                print('# 필수 입력사항입니다.')
            # 2. 이름이 중복된 경우
            elif player_name in player_list:
                print('# 이미 등록된 이름입니다.')
            # 3. 나쁜 이름인 경우
            elif player_name in ['돌아이', '멍멍이', '빡대가리']:
                print('# 해당 이름은 사용 할 수 없습니다.')
            else:
                player_list.append(player_name)
                print(player_list)
                break
            
    # print(f'\n{player_list[0+1]}의 턴!!')
    # print('[ 숫자를 입력하세요(최소 1개, 최대 3개) | 예시 : 23 24 25 ]')
    # print('# 마지막에 31을 입력하는 플레이어가 패배합니다.')
    # print(f'\n 현재 1부터 입력하시면 됩니다!!')
    # print(number_list)
    # number = list(map(int, input('>>> ').split()))
    # number.append(number_list)
    # print(number_list)
