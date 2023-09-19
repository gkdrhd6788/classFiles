def func(n,cnt):
    global min_cnt
    if n == N-1:
        if min_cnt > cnt:
            min_cnt = cnt
        return

    for i in range(battery[n],0,-1):
        if min_cnt < cnt: continue
        func(n+i,cnt+1)


arr = list(map(int,input().split()))
N = arr[0]  # 정류장 수
min_cnt = N
battery = arr[1:]+[0,0,0,0,0,0,0,0,0,0,0]

func(0,0)
print(min_cnt-1)