
player_num = input('>>> ')

if not player_num.isdecimal():
        print('# 숫자로 쓰라 했다~~~')
        continue
else:
    player_num = int(player_num)

if player_num < 2 or player_num > 4:
    print('인원 범위가 알맞지 않음!(2 ~ 4 입력)')
    continue
            