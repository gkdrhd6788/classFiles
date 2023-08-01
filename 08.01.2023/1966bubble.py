def BubbleSort(a,N):
    for i in range(N-1,0,-1): # i 구간의 마지막 인덱스
        for j in range(0,i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))

    BubbleSort(arr,N)

    print(f'{tc}', *arr)   #*arr뜻 알아보기



