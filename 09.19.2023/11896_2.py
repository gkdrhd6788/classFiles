def func(n,cnt):
    global min_cnt
    if min_cnt <= cnt: return
    if n >= N-1:
        if min_cnt > cnt:
            min_cnt = cnt
        return

    for i in range(1,battery[n]+1):
        if n+i > N: return
        func(n+i,cnt+1)


for tc in range(1,int(input())+1):
    arr = list(map(int,input().split()))
    N = arr[0]  # 정류장 수
    min_cnt = N
    battery = arr[1:]

    func(0,0)
    print(f'#{tc} {min_cnt-1}')