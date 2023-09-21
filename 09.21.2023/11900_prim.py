import heapq
def prim(start):
    heap = []
    MST = [0]*(V+1)
    heapq.heappush(heap,(0,start))
    sum_weight = 0
    while heap:
        weight,v = heapq.heappop(heap)
        if MST[v] : continue
        MST[v]= 1
        sum_weight += weight
        for next in range(V+1):
            if graph[v][next] == 0 or MST[next]:continue
            heapq.heappush(heap,(graph[v][next],next))
    return sum_weight


for tc in range(1, int(input())+1):
    V, E = map(int,input().split())
    graph = [[0]*(V+1) for _ in range(V+1)]

    for _ in range(E):
        n1,n2,w = map(int,input().split())
        graph[n1][n2] = w
        graph[n2][n1] = w

    result = prim(0)
    print(result)