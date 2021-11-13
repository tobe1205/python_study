# 플레이어의 이름을 저장할 리스트
player_list = []
number_list = []


print('### 베스킨라빈스~~~ㅆㅓ리 원~!')
print('- 참여인원을 입력(최소2 최대 4)')

while True:

    player_num = int(input('>>> '))

    if player_num < 2 or player_num > 4:
        print('# 인원 범위가 알맞지 않음(2 ~ 4 입력)')
        continue
   
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
    while True:

        for player in player_list:
            idx = player_list.index(player)
            print(f'\n{player_list[idx]}의 턴!!')
            print('[ 숫자를 입력하세요(최소 1개, 최대 3개) | 예시 : 23 24 25 ]')
            print('# 마지막에 31을 입력하는 플레이어가 패배합니다.')
          
            print(f'\n 현재 --부터 입력하시면 됩니다!!') # 리스트의 마지막 인덱스를 가지고온다. number_list[-1] + 1
            
            print(number_list)
            
            number = list(map(int, input('>>> ').split()))  

            number_list.append(number)
            idx += 1
             
            # if : # 1. 전 사람이 마지막으로 입력한 번호에 다음번호부터 입력하지 않으면 '~부터 제대로 입력하세요' 문구 출력

            # elif : # 2. 순차적으로 입력하지 않으면 '순차적으로 입력하세요' 문구출력
            
            # elif : 3. 31을 말하면 패배
            # else:
            #     # 3. 정상적으로 입력했다면     
            #              
            
            
                

            


