# 다익스트라 아님. 다익스트라는 효율성을 위해 우선순위큐 사용

for tc in range(1, int(input())+1):
    N,E = map(int,input().split()) #마지막 번호 N,  간선갯수 E
    G = [[] for _ in range(N+1)]
    for _ in range(E):
        u,v,weight = map(int,input().split())
        G[u].append((v,weight))
    # 초기값 설정 중요!!
    # D[v] : 출발점에서 v정점까지 최단거리
    D = [0xfffff]*(N+1)
    D[0] = 0

    Q = [0]
    while Q:
        u = Q.pop()
        for v,weight in G[u]:
            # (u,v) 간선완화
            if D[v] > D[u]+weight:
                D[v] = D[u] + weight
                Q.append(v)

    print(f'#{tc} {D[N]}')


