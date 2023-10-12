t = int(input())
for tc in range(1,t+1):
    N,M = map(int,input().split())
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))
    max_total = -1e9
    if N < M: #arr2가 이동해야
        for i in range(M-N+1):
            total = 0
            for j in range(N):
                total += arr1[j]*arr2[j+i]
            if max_total < total :
                max_total = total
    else: # arr1이 이동해야
        for i in range(N-M+1):
            total = 0
            for j in range(M):
                total += arr1[j + i] * arr2[j]
            if max_total < total:
                max_total = total
    print(f'#{tc} {max_total}')