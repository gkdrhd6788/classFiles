# numbers = [1,3,5,6,7,9,10,11]
numbers = [1,3,5,7,9,11]
found_even = False

for num in numbers:
    if num %2 == 0 :
        print('첫번째 짝수는 :', num)
        found_even = True
        break

if not found_even :
    print('짝수를 찾지 못했습니다')

# else:
#     print('짝수를 찾지 못했습니다')