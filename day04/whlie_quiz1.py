

num = int(input('정수 1: '))
num2 = int(input('정수 2: '))

total = 0
sum = num

while sum <= num2:
    total += sum
    sum += 1

print(f"{num}~{num2}까지의 총합: {total}")

