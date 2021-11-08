

# ssn = (input('> '))

# firstNum = int(ssn[:6])
# backNum = int(ssn[7:])
# genderNum = int(ssn[7])

# if genderNum == 1 or genderNum == 3:
#     gender = '남성'
# elif genderNum == 2 or genderNum == 4:
#     gender = '여성'

#     print(f'주민번호 앞자리: {firstNum}')
#     print(f'주민번호 뒷자리: {backNum}')
#     print(f'년생 {ssn[2:4]}월 {ssn[4:6]}일 세 {gender}')



ssn = input('주민번호: ')
print(f'주민번호 앞자리: {ssn[:6]}')
print(f'주민번호 뒷자리: {ssn[7:]}')

# 출생년도 4자리, 월, 일, 나이, 성별
month = int(ssn[2:4])
day = int(ssn[4:6])
year_2 = int(ssn[:2]) # 2자리

# 뒷자리 성별코드 
gen_num = int(ssn[7])

if (gen_num == 1) or (gen_num == 2):
    year_4 = year_2 + 1900
else:
    year_4 = year_2 + 2000 

age = 2021 - year_4 + 1

if (gen_num) == 1 or (gen_num == 3):
    gender = '남성'
elif (gen_num) == 2 or (gen_num == 4):
    gender = '여성'

print(f'{year_4}년생 {month}월 {day}일 {age}세 {gender}')