
dog = '멍멍이'
cat = '야옹이'
print(dog, cat, '좋아요!',sep=' ') # 구분자 seperation
print(dog, cat, '좋아요!',sep='')
print(dog, cat, '좋아요!',sep='=>')
# sep = 옵션을 안쓰면 기본적으로 적용되는 것이고, sep = '' 공백을 주지않으면 띄어쓰기를 하지 않는다. 

print('=' * 40)

print(dog); print(cat) # 파이썬은 이어서 명령어를 쓰고싶으면 ; (세미콜론)을 사용해서 쓴다.

print(dog, end= '와')
print(cat)

gim = '김밥'
dan = '단무지'
bob = '볶음밥'

print(gim, dan, bob, sep='!!', end='=>맛있다\n') # \n을 붙어주지않으면 칸바꿈을 하지 않는다.
print(gim, dan, bob, sep = '!!',end = '=>맛있다')

 # 탈출 문자 (escape sequence)
 # \n: 줄바꿈, \t 들여쓰기 tap
print("\n\n안녕하세요!")
print("잘\t가\t\t!!")               

# <21.11.02> 
# 문자열 포맷팅
print("="*30)

idol = '방탄소년단'
bts = 7

print(idol + '은 ' + str(bts) + '명' + '입니다.')

print(idol, '은 ', bts, '명입니다', sep = '')

# %s: 문자를 넣을 때, %d: 정수, %f 실수 c언어기법
print('%s은 %d명입니다.' % (idol, bts))
print('{}은 {}명입니다.'.format(idol,bts))

month = 12
day = 25
anni = '크리스마스'

# 12월 25일은 크리스마스입니다.
print('%d월 %d일은 %s입니다.' %(month, day, anni))
print('{}월 {}일은 {}입니다.'.format(month,day,anni))
print(str(month) + '월 ' + str(day) + '일은 ' + anni + '입니다.')

print('=' * 30)

#f 는 자동으로 6자리까지 제한
pi = 3.14159265
print('원주율은 %.8f입니다' %(pi)) 
print('원주율은 {}입니다.'.format(pi))
print('원주율은 {:.2f}입니다.'.format(pi))

me = 'kim'
you = 'park'

print('{0} and {1} and {0}'.format(me, you))
print('{a} and {b} and {a}'.format(a = me, b= you))

print('=' * 30)

num = 1234

print('~~~%d~~~~' % num)
print('~~~%6d~~~~' % num)
print('~~~%-6d~~~~' % num)
print('~~~%-8d~~~~' % num)

for p in [30, 19600, 8700, 500, 25]:
    print('가격: %7d원' % p)


print('\n\n')
print('%-9s%-9s%-9s%-9s' % ('번호','이름','나이','부서'))
print('='*40)

print('~~~~{}~~~~' .format(num))
print('~~~~{:>8d}~~~~' .format(num))
print('~~~~{:>10d}~~~~' .format(num))
print('~~~~{:<10d}~~~~' .format(num))
print('~~~~{:<10d}~~~~' .format(num))
print('~~~~{:^10d}~~~~' .format(num))
print('~~~~{:^10d}~~~~' .format(num))


 