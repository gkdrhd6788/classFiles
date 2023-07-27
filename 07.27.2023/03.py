
while True: 
    try:
        num = int(input('100으로 나눌 값을 입력해'))
        print(100/num)
        break #while True에서 빠져나감
    # except (ValueError,ZeroDivisionError) : 
    #     print('제대로 입력해라')

    except ValueError : #클래스 이미 지정됨
        print('숫자를 입력하라고')

    except ZeroDivisionError :
        print('왜 0을 입력하는거야?')

    except : #우리가 미처 생각하지 못한 에러를 위해)
        print('에러가 발생했어')




'''
#try- except안쓰면 if else써야 함
while True:  
    num = input()

    if num == 0:
        print('0말고 다른거 입력해')
        continue

    if num.isdigit():
        num = int(num)
        break


    else: 
        print('숫자가 아니야')
        continue
'''
    
    
