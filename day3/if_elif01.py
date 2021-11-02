
 # 파이썬에서는 else if 라고 하지않고 elif 를 사용한다. 자바와 헷갈리지 않게 조심하자!!
age = int(input('나이: '))

if age >= 20:
    print('성인입니다.')
elif age >= 17:
    print('고등학생입니다.')
elif age >= 14:
    print('중학생입니다.')
elif age >= 8:
    print('초등학생입니다.')
else:
    print('미취학 아동입니다.')

