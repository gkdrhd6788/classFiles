def perm(n,total):
    global min_total
    if min_total < total: return
    if n == N:
        # print(total)
        # if min_total > total:
        min_total = total
        return

    for i in range(N):
        if used[i]==1:continue
        # permlist[n] = arr[i]
        used[i]=1
        perm(n+1,total+arr2[n][i])  # permlist사용안해도 됨
        used[i]=0

for tc in range(1,int(input())+1):
    min_total = 100*16
    N = int(input()) # 제품수
    # arr = [i for i in range(N)]
    # print(arr)
    arr2 = [list(map(int,input().split())) for _ in range(N)]  # 각 제품당 공장별 생산비용
    # permlist = [0]*N
    used = [0]*N
    perm(0,0)

    print(f'#{tc} {min_total}')