##N=input()
##total=0
##numList=list(map(int,input().split()))
##for i in numList:
##    if i%2!=0:
##        total=total+i
##print(total)



#한번에 줄바꿈으로 여러 줄의 숫자 입력 가정
#N=int(input())
##massList=input().split("\n")   #[3 17 1, 22 8 5, 6 63 2]
##print(massList)
##for numbers in massList:   #aList = 3 17 1 string
##    print(numbers)
##    numList=list(map(int,numbers.split()))
##    total = 0
##    for i in numList:
##        if i%2 != 0 :
##            total = total + i
##    print(total) 

##3 17 1 39 8 41 2 32 99 2
##22 8 5 123 7 2 63 7 3 46
##6 63 2 3 58 76 21 33 8 1 



#input이 여러번일 때 가정
N = int(input())
for n in range(N):
    aList = list(map(int,input().split())) #map은 for문 못돌리나?
    total = 0
    for i in aList:
        if i%2 != 0 :
            total = total + i
    print(f"# {n+1} {total}")
