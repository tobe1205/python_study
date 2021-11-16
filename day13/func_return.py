############################
#  함수 정의
def add(n1,n2):
    print(f'{n1},{n2}')
    return n1 + n2 # return은 함수의 탈출문! 즉시 종료
    a = 10

def sub(n1,n2):
    res = n1 - n2
    return res

def multi(n1,n2):
    print(f'{n1} x {n2} = {n1 * n2}')

def infinite_loop():
    while True:
        msg = int(input('>>> '))

        if msg == 0:
            print('break!!!')
            break
        elif msg == 1:
            print('continue!!')
            continue
        elif msg == 2:
            print('return!!')
            return

        print('하하호호')
    print('함수 이제 끝남')


def operate_all(n1, n2):
    # return[n1+n2, n1-n2, n1*n2, n1/n2]
    return {
        'add': add(n1, n2)
        , 'sub': sub(n1, n2)
        , 'mul': n1 * n2
        , 'div': n1 / n2
    }


    # return[add(n1,n2), sub(n1-n2), n1*n2, n1/n2] 와 같다.



############################
# 실행부

if __name__=='__main__':

    print(add(10, 5))

    add(100, 200)
    result = add(100, 200)
    print(result)
    
    result2 = sub(100,20)
    print(result2)

    multi(3, 7)

    # 중첩이 가능하고 안쪽부터 실행된다. 
    result3 = add(add(add(2,3), 8), 11)
    print(result3)

    # add(multi(3,3), sub(20, 10)) 리턴이 없는 multi 함수로 인해 오류 발생
    add(sub(3,3), sub(20, 10))

    multi(add(4, 7), sub(10, 4))

    print('=' * 40)

    # infinite_loop()
    result_list = operate_all(10, 5)
    print(result_list[2])