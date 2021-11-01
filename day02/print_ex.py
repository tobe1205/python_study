
dog = '멍멍이'
cat = '야옹이'
print(dog, cat, '좋아요!',sep=' ')
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

print(gim, dan, bob, sep='!!', end='==>맛있다')