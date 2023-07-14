strNum=input()

number=int(strNum)
if number<10:
    print(number)
elif 10 <= number < 100 :
    print(int(strNum[0])+int(strNum[1]))
elif 100 <= number < 1000 :
    print(int(strNum[0])+int(strNum[1])+int(strNum[2]))
elif 1000 <= number < 10000 :
    print(int(strNum[0])+int(strNum[1])+int(strNum[2])+int(strNum[3]))

