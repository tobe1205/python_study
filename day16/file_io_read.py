

file_path = 'D:/isec_kgw/py_study/멍멍이.txt'

try:
    f = open(file_path, 'r')
    data = f.read()
    print(data)

except:
    print('파일 로드 실패!')

finally:
    f.close()

print('=' * 40)

try:
    f = open(file_path,'r')
    while True:
        str = f.readline()
        print(str, end='')
        if len(str) == 0 : break

except:
    print('파일 로드 실패!')

finally:
    f.close()