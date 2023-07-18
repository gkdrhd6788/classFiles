"""
시퀀스의 특징!!5가지
순서 인덱싱 슬라이싱 길이 반복
"""

"""단축평가 중요
"""

# 진법 변경
print(bin(12)) # 2진법
print(oct(12)) # 8진법
print(hex(12)) # 16진법



#Floating point rounding error
a = 3.2 -3.1    # 0.10000000000000009
b= 1.2 - 1.1    # 0.09999999999999987
print(a)
print(b)

#실수 연산 시 해결책 No.1- 임의의 작은 수 활용
print(abs(a-b) < 1e-10) #True

#실수 연산 시 해결책 No.2- math 모듈 활용
import math
print(math.isclose(a,b))



#지수 표현 방식 e = 10
number = 314e-2
number = 314E-2 # e == E
print(type(number)) 



#Escape Sequence
print("줄 \"바꿔서\" 나오게") # " " 안에  " " 출력 방법
print("이 다음은 \\엔터입니다.")  #\출력 방법



# f-string 
bugs = 'roaches'
counts = 100
area = 'living room'
print(f'Debugging {bugs} {counts} {area}') 

print('Debugging {} {} {}'.format(bugs,counts,area)) #f-string 나오기 전1
print('Debugging %s %d %s' %(bugs,counts,area)) #f-string 나오기 전2



# f-string advanced
greeting = 'hi'
print(f'{greeting:^10}') #10의 공간을 주고 가운데 정렬
print(f'{greeting:>10}') #10의 공간을 주고 오른쪽 정렬
print(f'{3.141592:.4f}') #4자리까지만 출력 (f-string advanced검색 가능)


my_str = 'hello'
print(my_str[1])
print(my_str[1:3]) #강사님 팁: 사이사이를 기준으로 파악
print(my_str[:3])
print(my_str[3:])
print(my_str[0:0:2]) # 건너뛰기
print(my_str[::2])   # 건너뛰기(상동)
print(my_str[::-1])  #거꾸로
print(len(my_str)) #길이

# my_str[1] = 'z'  이렇게 문자열 변경 불가 
#해결책: 새로운 문자열 생성(아래 참고)

'''
 string        불변
 list = [ ]    가변 , 모든 데이터 타입이 들어갈 수 있음
 tuple = ( )   불변--리스트와의 차이점
                ( ) 생략도 가능
                개발자가 직접 사용하기보다 파이썬 내부 동작에서 사용됨-->중요x

 range         불변
 
 '''

my_tuple_1 = (1, )   #tuple안에 1개만 있으면 ' , '  해줘야!!안그럼 정수와 같아짐
my_range_1 = range(5)
print(my_range_1)           #range(0, 5)
print(list(my_range_1))     #[0, 1, 2, 3, 4]

'''
Non-sequence
dict = { }      순서x 중복x 가변
                key는 불변의 자료형(str,tuple,range,int,float...)만 사용가능, 
                value는 모든 자료형 가능

set             순서x 중복x 가변
                key와 value의 쌍이 아님
                집합연산 가능

'''

my_dict = {'apple':12, 'list': [1,2,3] }
print(my_dict['apple']) #value를 추출하는 법
my_dict ['apple'] = 20
print(my_dict)          #{'apple': 20, 'list': [1, 2, 3]}



#set의 특징 이해
my_set_1 = set() # 아무것도 없는 set는 이렇게 만들어줘야. {}로 만들면 dict이 됨
my_set_2 ={1,2,3}
my_set_3 ={3,6,9}
my_set_4 ={1,1,1}

print(my_set_1) 
print(my_set_2) #{1, 2, 3}  순서가 없기 때문에 2번째 이런게 없고  index가 없음
print(my_set_4) #{1}   중복이 없기 때문에 요렇게 된다.



# set 집합연산
print(my_set_2 | my_set_3)  # 합집합
print(my_set_2 - my_set_3)  # 차집합
print(my_set_2 & my_set_3)  # 교집합

#기타 None
variable = None
print(variable)
print(type(variable)) 



#  Collection : 여러 개의 항목을 담는 자료구조(Sequence상관 없이)
#  ex. str, list, tuple,set, dict

#불변과 가변 비교
my_str = 'hello' #하나의 메모리 주소에 'hello' )(python tutor보면 이해 쉬움)
# my_str [0] = 'z'
my_list =[0,1,2,3] # 각 값이 나뉘어서 메모리 주소가 있음
my_list[0]=100

#가변 데이터들의 주의사항 
list_1 = [1,2,3]
list_2 = list_1 
list_1[0] = 100 
print(list_1) # [100, 2, 3]
print(list_2) # [100, 2, 3] python tutor 보면 이해 쉬움

# 불변 데이터와 ex.int 와의 차이점
a = 10
b = a
a = 20
print(a,b) # 20,10

#암시적 형변환
print(True)         # True
print(True+1)       # 2  (왜냐면 True = 1 )
print(True+False)   # 1
print(3+5.0)        # 8.0 ( 3이 3.0으로 바뀜 )

#명시적 형변환
int(3.5)
# int('3.5')  에러뜸  해결책: int(float('3.5'))

print( tuple([1,2,3]))
print( tuple('string'))
print( tuple({1,2,3}))
print(tuple({'key1':1,'key2':2})) #key만 나옴
print(tuple(range(3))) 

print(8/2)  #파이썬은 유독 나누기만 항상 실수가 나옴


#자릿수 구하는 법
num = 1234
while num > 0:
    print( num % 10 )
    num //= 10

#비교 연산자 --숫자 뿐만 아니라 문자도 비교 가능
# ==        -- 값이 갖은지 판단(Equality 동등성)     주의!! 2.0==2(묵시적 형변환)
# is, is not -- 메모리 내에서 같은 객체를 참조하는지 확인
#               Identity(식별성)                    주의!! 2.0 is 2 false
#               갖은 주소를 갖는 지 여부(객체끼리 비교할 때)

print('a'>'A')    # True  사전상에서 나중에 오는 것이 큰 것
print('가'>'나')  # False

#논리 연산자
# and  둘다 True
# or   둘 중 하나 True
# not 
print(not 0) # True
print(not True)