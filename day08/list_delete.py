# 리스트안의 내용 삭제

greetings = ['안녕', '헬로', '곤니치와', '니하오']
print(greetings)

greetings.remove('헬로')
print(greetings)

del(greetings[1])
print(greetings)

# 전체삭제
greetings.clear()
print(greetings)