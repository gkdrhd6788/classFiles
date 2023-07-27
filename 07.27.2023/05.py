def f():
    print('f() 실행')
    raise Exception('예외 발생') #강제로 exception발생시키는 것
    print('f() 끝')
def g():
    print('g() 시작')
    f()
    
    print('g() 끝')

def h():
    print('h() 시작')
    try :  #객체지향에서 등장! 이전에는 if-else로 복잡하게 처리했음
        g()
    except: #아무것도 안적으면 모든 에러 잡는것
        print('잡았다 요놈')
    print('h() 끝')

h()
print('종료')

'''
def f():
    print('f() 실행')
    raise Exception('예외 발생') #강제로 exception발생시키는 것
    print('f() 끝')
def g():
    print('g() 시작')
    f()
    print('g() 끝')

def h():
    print('h() 시작')
    try :  #객체지향에서 등장! 이전에는 if-else로 복잡하게 처리했음
        g()
    except: #아무것도 안적으면 모든 에러 잡는것
        print('잡았다 요놈')
    print('h() 끝')

h()
print('종료')
'''

#전파되다가 프로그램이 종료된다.??
