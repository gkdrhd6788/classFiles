# B높이 선반
# N명의 점원
# 각 점원의 키 H
# 점원의 키를 최소한으로 더하기
# 최소한의 B의 값을 알기!!
# 알고리즘 1. 완전탐색 트리ox, 백트래킹(최소값을 넘으면)
def fun(n, t):
    global min_t
    # 가지치기1
    if min_t < t: return
    # 가지치기2
    if B <= t :
        min_t = t
        return

    # 직원의 키를 더했을 떄
    fun(n + 1, t + height[n])
    # 직원의 키를 더하지 않았을 때
    fun(n + 1, t)


T = int(input())
for tc in range(1, T+1):
    N,B = map(int,input().split()) ## N명의 점원   B높이 선반
    height = list(map(int,input().split()))  # # N명 각 점원의 키 H
    min_t = 10000*21
    fun(0,0)
    print(f'#{tc} {min_t-B}')