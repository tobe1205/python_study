

# 리스트 인덱싱

tvxq = ['영웅재중', '최강창민', '유노윤호', '믹키유천', '시아준수']

print(tvxq[2])

print(type(tvxq))
print(type(tvxq[0]))

print(tvxq[1].find('창'))
print(tvxq[1][3])
print(tvxq[3][:2])

# 리스트 슬라이싱

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] #range(10) 
print(nums[2:5:1]) # 뒤에 1 생략가능
print(nums[:4])
print(nums[6:][1])

result = nums[5] + nums[2:7][3]
print(result)

print(type(nums[2:5]))
print(type(nums[3]))

# 리스트는 인덱싱을 통해 변수처럼 내부값을 변경할 수 있다.
print('='* 40)
tvxq[2] = '아이노유노'
print(tvxq)

tvxq[4] = tvxq[0][:2]
print(tvxq)

# 문자열은 인덱싱을 통한 수정이 불가능한 리스트
s ='hello'
# s[2] = 'x' # hexlo

s = s.replace('l', 'x', 1)
print(s)


# unpackaging: 리스트 내부 데이터를 다시 변수에 따로 저장
# 좌항의 변수 갯수와 우항의 리스트 데이터 갯수가 일치해야 함

# tvxq = ['영웅재중', '최강창민', '유노윤호', '믹키유천', '시아준수']


hero, max, yuno, micky, xia = tvxq
print(max)

'''
hero = tvxq[0]
max = tvxq[1]
yuno = tvxq[2]
micky = tvxq[3]
xia = tvxq[4]
'''


# 리스트의 +, * 연산
print('='*40)
list1 = [1,2,3,4,5]
list2 = [10,11,12]

print(list1 + list2)
print(list2 + list1)

print(list2 * 3) # 리스트 * 정수 

print(list1) # 원본은 변하지 않는다.

# 빈 리스트 만들기
empty = []
empty = list()






