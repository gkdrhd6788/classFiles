try:
    num = int(input('100으로 나눌 값을 입력해'))
    print(100/num)
# except (ValueError,ZeroDivisionError) : #클래스 이미 지정됨
#     print('제대로 입력해라')

except BaseException : #클래스 이미 지정됨
    print('숫자를 입력하라고')
    

except ZeroDivisionError :
    print('왜 0을 입력하는거야?') #숫자를 입력하라고(z는 b의 하위클래스)

except : #우리가 미처 생각하지 못한 에러를 위해)
    print('에러가 발생했어')