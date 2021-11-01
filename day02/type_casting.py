
name = "홍길동" 
score = 78 

print(name + "님의 점수는 " + str(score) + "입니다.") 

print(type(score))

n1 = 10
n2 = '34'

# print(str(n1)+ n2) # 문자와 문자는 더하는것이 아닌 결합이 된다.

print(n1 + int(n2))

# # 타입 변환 함수는 일시적 변환일 뿐 실제값은 변하지 않는다.

print('=============================')

print(type(n2))

n2 = int(n2)
print(type(n2))

# 변환대상이 정수로 바뀔 수 없는 값이면 에러발생
# int('hello')

s = '2.33'
print(float(s))

# 반올림할 때는 round() 함수를 활용
print('===========================')

print(round(4.78))
print(round(4.18))
print(int(4.18)) # 정수형이라 소숫점 이하 버림
print(round(4.67812345678944)) # 소숫점 첫째자리에서 반올림되고 소숫점 이하 버림
print(round(4.67812345678944, 2)) # 두번째 자리에서 반올림을 하고싶다면, ,후에 해당 자리 입력
