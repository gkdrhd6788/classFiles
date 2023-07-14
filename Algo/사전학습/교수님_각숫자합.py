strNum=input("1에서부터 9999까지의 자연수를 입력하시오:")

sum=0

for i in strNum:
    #print(i,type(i))
    a = int(i)
    sum=sum+a
    
print(sum)
