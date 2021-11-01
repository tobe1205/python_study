
# 산술 연산자
a, b = 18, 4
print(a / b)
print(a // b)
print(a % b)

#  4 % 10 -> 몫: 0 , 나머지: 4 // 앞숫자가 더 작으면 앞숫자가 나머지
# 0 % 7  -> 몫: 0, 나머지: 0 
# 7 % 0 -> 연산불가 : 에러발생

print(3 ** 2)
print(2 ** 4)

# 복합대입연산자 
print('=======================')

a = 5

a += 1 # a = a + 1 (a에 1을 더해서 대입해라)
print(a) 

a -= 2
print(a)

a *= 3
print(a)

a //= 5
print(a)

a **= 5
print(a)

# a =+ 20 : a = +20 (양수 20을 a에 대입하시오 =은 항상 우측에 와야한다.)

# 선언되지 않은 변수는 복합대입을 사용할 수 없다.
# c +=2 # c = c + 2) 파이썬에서는 ++i; --i; 가 없다.

# 관계 연산자
print('=======================')

d = 5
print(d < 6)
print(d >= 10)
print(d == 5)

e = d == 7 - 2 # 우선순위를 잘 모르면 ()로 우선순위를 바꿔주자
print(e)
print(type(e))

# 문자열 비교
print('========================')

print('ace' < 'ade')
print('apple' < 'grape')
print('zebra' < '감자')
print('짜장면' < '김밥')

password = 'abc1234'
print(password == 'ABC1234')

# 문자열 특수 연산 (파이썬에서만) "문자 x 정수" 만 가능!
s1 = '메롱'
print(s1 * 3)
print('=' * 30)