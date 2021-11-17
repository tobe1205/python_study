

def get_max(numberlist1):
    max = numberlist1[0]
    for n in numberlist1:
        if max < n:
            max = n
    return max 


def get_max2(numbers):
    numbers.sort(reverse=True)
    return numbers[0]

def get_max3(numbers):
    return max(numbers)    


print("-" * 40)

data_list = list(map(int, input("정수: ").split(" ")))

print("최대값: {}".format(get_max(data_list)))   