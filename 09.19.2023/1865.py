def punc(n,total):
    global max_total
    if max_total >= total: return
    # if total == 0: continue

    if n == N:
        # print(punclist,end=' ')
        # print(total)
        # if max_total < total:
        max_total = total
        return
    for i in range(N):
        if used[i]==1: continue
        punclist[n] = nums[i]
        used[i] = 1
        punc(n+1,total*arr[n][punclist[n]]/100)
        used[i] = 0


for tc in range(1,int(input())+1):
    max_total = -1
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    nums = [i for i in range(N)]
    punclist = [0]*N
    used = [0]*N

    punc(0,1)
    print(f'#{tc} {max_total*100:6f}')