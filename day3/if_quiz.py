

kor = int(input('국어: '))
math = int(input('수학: '))
english = int(input('영어: '))

average = (kor + math + english) / 3
# average = round(average, 2)
print('당신의 평균점수: {:.2f}점'.format(average))

if average >= 60:
    
    print('당신은 시험에 통과하였습니다.')

else:
    print('재수강 대상자입니다.')

print('열공하세요!') # 종속에서 벗어나서 항상 출력된다.