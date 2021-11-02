

n1 = 10
result = 10 + 20 # = 은 같다라는 의미가 아닌, 대입연사자로, 우측의 항을 좌측에 대입 or 저장한다 라는 의미로 해석
print(result * 3)

result = n1 + 20
print(result)

# 선언(make)되지 않은 변수는 사용 불가!
# result = number + 10
# print(number)
print("number") # 따옴표안에 있으면 전부 텍스트로 취급(변수 X)

fruit = '사과'

print(fruit + ' 맛있어요~')

print('=============================')

# 변수 이름 규칙
# 1. 숫자로 시작하면 안된다. (모든 프로그래밍 공통)
# 7number = 700  - 에러
number7 = 700 # 처음만 아니면 어느곳에 숫자가 위치해도 상관없다.
num7ber = 777

# 2. 공백을 포함할 수 없다.
# user birth day = 19921205
userbirthday = 19921205
user_birth_day = 19921205 # snake case 띄어쓰기마다 "_" 이용(파이썬 선호)
UserBirthDay  = 19921205  # camel case 앞글자마다 대문자 입력(자바, 자바스크립트 선호)

# 3. 대/소문자를 구분한다.
banana = '바나나'
BANANA = '뻐네이너'

print(BANANA)

# 4. if , while과 같은 이미 기능이 포함된 단어는 변수이름 사용할 수 없다.
# if = 123
# for = '메롱'

# 한글, 한자변수 가능? - 가능하지만 안쓰는걸 강력권고!!
야옹이 = '고양이'
print(야옹이)

# print()와 같은 내장함수의 이름은 변수이름으로 지정가능하나, 그 기능을 더이상 활용할 수 없다.
# print = 500
# print();

#  a = 10
#  b = 20
a, b = 10, 20; # 파이썬만 이 방법으로 가능
print(a + b) 

