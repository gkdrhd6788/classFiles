N=int(input())
for i in range(N):
    numList = list(map(int,input().split()))
    numList.sort()
    print(f"#{i+1} {numList[-1]}")
