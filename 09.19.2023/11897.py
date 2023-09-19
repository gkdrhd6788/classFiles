def perm(n):
    global min_total
    if n == N:
        total = 0
        for j in range(N): # [0,1,2] 제품1은 0은 0번째 공장에서 생산, 2는 1번쨰 공장
            total += arr2[j][permlist[j]]
        print(permlist,end = ' ')
        print(total)
        if min_total > total:
            min_total = total

        return

    for i in range(N):
        if used[i]==1:continue
        permlist[n] = arr[i]
        used[i]=1
        perm(n+1)
        used[i]=0



for tc in range(1,int(input())+1):
    min_total = 100*16
    N = int(input()) # 제품수
    arr = [i for i in range(N)]
    # print(arr)
    arr2 = [list(map(int,input().split())) for _ in range(N)]  # 각 제품당 공장별 생산비용
    permlist = [0]*N
    used = [0]*N
    perm(0)

    print(f'#{tc} {min_total}')