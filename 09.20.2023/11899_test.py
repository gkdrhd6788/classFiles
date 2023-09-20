def find_set_recur(x):
    if x==p[x]:
        return p[x]
    else:
        p[x] = find_set_recur(p[x])
        return p[x]

for tc in range(1,int(input())+1):
    N,M = map(int,input().split())  # N개의 출석번호, M장의 신청서
    arr = list(map(int,input().split()))
    p = [i for i in range(N+1)]  # 1번부터 N번까지
    ans = N  #최초 집합의 개수
    for i in range(0,M*2,2):
        u,v= arr[i],arr[i+1]
        a = find_set_recur(u)
        b = find_set_recur(v)
        if a == b:
            continue
        p[b] = a
        ans -= 1
    print(f'#{tc} {ans}')