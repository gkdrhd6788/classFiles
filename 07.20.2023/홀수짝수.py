num_1 = int ( input ( "숫자를 입력하세요:" ) )
if num_1 % 2 !=0 :    #if num%2 : 도 같다 (num%2는 1이고 True이므로)
    print(f'{num_1}은 홀수입니다.')
else :
    print(f'{num_1}은 짝수입니다.')
print(num_1)