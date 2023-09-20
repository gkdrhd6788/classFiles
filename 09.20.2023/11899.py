# 연산
# find_set_반복문
def find_set(x):
    while x!=p[x]:
        x = p[x]
    return x

# find_set_재귀
def find_set_recur(x):
    if x==p[x]:
        return p[x]
    else:
        p[x] = find_set_recur(p[x])
        return p[x]

# 간단하게
def find_set_recur_2(x):
    if x != p[x]:
        p[x] = find_set_recur_2(p[x])
    return p[x]

def union(x,y):
    # 1. 이미 같은 집합인지 체크
    x = find_set(x)
    y = find_set(y)
    if x==y:
        return
    # 2. 다른 집합이라면, 같은 대표자로 수정 (그냥 parent[y]=x해도 됨)
    if x < y:
        p[y] = x
    else:
        p[x] = y
for tc in range(1,int(input())+1):
    N,M = map(int,input().split())  # N개의 출석번호, M장의 신청서
    arr = list(map(int,input().split()))
    p = [i for i in range(N+1)]  # 1번부터 N번까지
    ans = N  #최초 집합의 개수
    for i in range(0,M*2,2):
        u,v= arr[i],arr[i+1]
        a = find_set(u)
        b = find_set(v)
        if a == b:
            continue
        p[b] = a
        ans -= 1
    print(f'#{tc} {ans}')