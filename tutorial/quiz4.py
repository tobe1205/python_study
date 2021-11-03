

# age = int(input("몇살이에요? "))

# if age > 19:
#     print('당신은 성인입니다.')
#     print('주류를 구매할 수 있습니다.')

# else: 
#     print('당신은 성인이 아닙니다.')
#     print('주류를 구매할 수 없습니다.')

# print()
# print('=' * 40)

# kor = int(input('국어: '))
# eng = int(input('영어: '))
# meth = int(input('수학: '))

# avg = (kor + eng + meth) / 3 
# print('당신의 평균점수: {:.2f}점'.format(avg))

# if avg >= 60:
#     print('이번시험에 통과했습니다.')

# else:
#     print('재수강 대상자입니다.')

# print('열공하세요!') 


# num = int(input('정수: '))

# if num == 0:
#     print('입력하신 숫자는 0입니다.')
# elif num % 7 == 0:
#     print('입력하신 숫자는 7의 배수입니다.')
# else:
#     print('입력하신 숫자는 7의 배수가 아닙니다.')


print('***** 점수 관리 프로그램 *****')
point = int(input('점수를 입력하세요: '))

if point >= 90:
    if point > 100:
        print('점수를 잘못 입력했습니다.')
    elif point >= 95:
        print('당신의 학점은 A+입니다.')
    else: 
        print('당신의 학점은 A입니다.')
elif point >= 80:
    print('당신의 학점은 B입니다.')
elif point >= 70:
    print('당신의 학점은 C입니다.')
elif point >= 60:
    print('당신의 학점은 D입니다.')
else:
    print('당신의 학점은 F입니다.')
    
