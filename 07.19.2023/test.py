def print_info(**kwargs):
    print(kwargs)

print_info(name ='alice', age =30)







print('hello',end =' ')
'''
기본인자 변경
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
'''
print('hi')







num= 100
def my_func():
    print(num)
my_func()   # 로컬에서 밖으로 갈 수 있지만,,좋은 코드가 아님




sum = 10    # built in 함수를 global 에서 변수로 써버림
print(sum)
#print(sum([1,2,3])) #안쪽에서 밖으로 찾아가므로 global에서 먼저 찾아버리므로
#built in에 있는 sum 함수에 접근 불가
# 'int' object is not callable

numbers =[1,2,3]
result = map(str, numbers)
print(result) # <map object at 0x0000020B1AEA95B0>
print(list(result)) # ['1', '2', '3']



def my_func(x):
    result = x*2
    return result
result_2 = map(my_func, numbers)
print(list(result_2))



#람다 함수의 필요성(map+lambda)
numbers = [1,2,3,4,5]
result = list(map(lambda x:x*2,numbers)) #일회성으로 쓸 때 
print(result)


# 어제 자 
#튜플의 이해
t_1 = 1,2,3
print(t_1)
t_2 = t_1 + (4,5)
print(t_2)
