

'''
point.txt를 읽어들여서
점수의 총점과 평균을 구한 후 
총점과 평균을 적어서 result.txt에 저장
'''

dir_name = 'D:/isec_kgw/py_study/'


try: 
    f = open('D:/isec_kgw/py_study/point.txt', 'r')
    point_str = f.read()

    points = point_str.split(',')
  
    total = 0
    for n in points:
        total += int(n)
    avg = total / len(points)


except:
    print('파일 로드 실패')
finally:
    f.close()  


try: 
    f = open('D:/isec_kgw/py_study/result.txt', 'w')
    
    data = f'총점: {total}점, 평균: {round(avg, 2)}점'
    
    f.write(data)
    

except:
    print('파일 쓰기 실패')
finally:
    f.close()  