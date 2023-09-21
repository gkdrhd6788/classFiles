'''
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''
# BFS구조와 비슷
import heapq

def prim(start):
    heap = [] # 비어있는 리스트
    # MST에 포함되었는지 여부
    MST = [0]*V
    # 가중치, 정점정보
    heapq.heappush(heap,(0,start))
    sum_weight = 0
    while heap:
        # 가장 적은 가중치를 가진 정점을 꺼냄
        weight,v = heapq.heappop(heap)
        # 이미 방문한 노드라면 패스
        if MST[v]: continue
        MST[v] = 1
        sum_weight += weight
        for next in range(V):
            if graph[v][next] ==0 or MST[next]: continue
            heapq.heappush(heap,(graph[v][next],next))
    return sum_weight




V,E = map(int,input().split())
# 인접행렬
graph =[[0]*(V+1) for _ in range(V+1)]
for _ in range(E):
    f,t,w = map(int,input().split())
    graph[f][t] = w
    graph[t][f] = w

result = prim(0)
print(result)