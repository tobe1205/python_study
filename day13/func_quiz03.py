
def get_max(*numbers):
    num = 0
    for n in numbers:
        num += n    
    return max(num) 





print('='*40)


data_list = list(map(int(input('정수: ').split)))

print('최대값: {}'.format(get_max(data_list)))