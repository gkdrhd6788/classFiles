def print_hello(x):
    return 'hello'+ x
    
map(print_hello, [1,2,3])




def print_hello(x,y):   #1,4 형식으로 들어감
    print('hello'+ x)
    return x*y
list ( map(print_hello, [1,2,3],[4,5,6]))
