inch = 2.54 # 1인치에 대한 cm값 지정

# 인치를 cm으로 변환해주는 함수

def convert_inch_to_cm(number):
    return number * inch

def info():
    print('안녕~~메롱!!')


###################
print('__name__의 값(custom.py):', __name__)

if __name__== '__main__':
# 실행테스트
    print('__name__의 값(custom.py):', __name__)
    print(convert_inch_to_cm(1))
    info()
    info()
    