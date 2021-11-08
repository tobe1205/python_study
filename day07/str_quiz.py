

ssn = input('주민번호: ')

month = ssn[2:4]
day = ssn[4:6]
gen_num = int(ssn[7])
year_2 = int(ssn[:2])

print(f'주민번호 앞자리: {ssn[:6]}')
print(f'주민번호 뒷자리: {ssn[7:]}')

if (gen_num == 1) or (gen_num == 2):
    year_4 = year_2 + 1900
else:
    year_4 = year_2 + 2000

age = 2021 - year_4 + 1

if (gen_num == 1) or (gen_num == 3):
    gender = '남성'
elif(gen_num == 2) or (gen_num == 4):
    gender = '여성'   


print(f'{year_4}년생 {month}월 {day}일 {age}세 {gender}')