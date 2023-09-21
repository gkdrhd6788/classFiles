import heapq
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
    pq = []
    heapq.heappush(pq,(0,0))
    while pq:
        dist,now = heapq.heappop(pq)
        if D[now] < dist : continue

        for v,weight in G[now]:
            total_weight = dist+weight
            if D[v] <= total_weight: continue
            D[v] = total_weight
            heapq.heappush(pq,(total_weight,v))


    print(f'#{tc} {D[N]}')


