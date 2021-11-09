

nums = [1,3,5,7]
print(nums)

# nums[4] = 9 (x)
nums.append(9)
print(nums)

nums.append('안녕')
print(nums)

nums.insert(2, 4) # 2번 인덱스로 4를 삽입
print(nums)
 
nums.insert(4, '메롱') # 2번 인덱스로 4를 삽입
print(nums)
'''
print('\n' * 40)
print('# 먹고 싶은 음식을 입력하세요~~')
print("[그만 입력하려면 '배불러' 라고 입력하세요.]")

food_list = []

while True: 
    
    menu = input('> ')

    if menu == '배불러':
        break
       
    else:
        food_list.append(menu)

print('입력을 종료합니다')
print(f'내가 먹고싶은 음식: {food_list}')

'''

        
        

