# 수영장(재귀)__지훈DP처럼 풀어보기
# 최소비용
# 알고리즘
# 완전탐색, 가지치기

def func(n,total):
    global min_total
    # 가지치기
    if min_total < total: return
    # 기저조건
    if n >= 12:
        min_total = total
        return

    # 1일 이용권 사용시
    func( n+1 , total + plan[n]*day )
    # 1달 이용권
    func( n+1 , total + month )
    # 3달 이용권
    func( n+3, total + three )
    # 1년 이용권
    func(n+12, total + year)



T = int(input())
for tc in range(1,T+1):
    min_total = 1e9
    day,month,three,year = map(int,input().split())
    plan = list(map(int,input().split()))
    func(0,0)
    print(f'#{tc} {min_total}')