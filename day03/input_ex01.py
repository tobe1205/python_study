

print('='* 40)

name = input("당신의 이름: ")
age = int(input("당신의 나이: "))

print('='* 40) 

print(f'{name}님 환영합니다!!!') # f-string 사용. - python 3.6버전 이상에서만 가능하다.
print(f'당신의 나이는 {age}이군요!')
# print('당신의 나이는 {}이군요!'.format(age))

# print(f'age의 타입: {type(age)}')

# input은 입력값을 무조건 str타입으로 처리한다.
print('당신의 나이는 {}년생이군요!'.format(2021-int(age)+1))

print('당신의 나이는 {}년생이군요!'.format(2021-age+1)) 
#위에 age란 변수에 값을 넣기전에 int로 변환해서 저장하게되면 format 명령어 안에 age는 int로 변환 할 필요 x


