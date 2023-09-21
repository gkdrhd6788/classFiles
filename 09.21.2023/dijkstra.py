'''
6 8
0 1 2
0 2 4
1 2 1
1 3 7
2 4 3
3 4 2
3 5 1
4 5 5
'''

# 내가 갈 수 있는 경로 중 누적거리가 제일 짧은 것부터 고르자!
# 우선순위 큐 사용하므로
import heapq
N,M = map(int,input().split())
# 인접리스트
graph =[[] for  i in range(N)]
for _ in range(M):
    f,t,w = map(int,input().split())
    graph[f].append([t,w]) #단방향


# 1. 누적거리를 계속 저장
INF = int(1e9)  # 최대값으로 1억-대충 엄청 큰 수
# distance[v] : 출발점에서 v정점까지 최단거리
distance =[INF]*N

def dijkstra(start):
    # 2. 우선순위 큐
    pq = []
    heapq.heappush(pq,(0,start))
    distance[start]=0
    while pq:
        # 누적거리가 가장 짧은 노드에 대한 정보 꺼내기
        dist,now = heapq.heappop(pq)
        # 이미 방문한 지점+ 누적거리가 더 짧게 방문한 적이 있다면pass
        if distance[now] < dist: continue
        # 인접 노드를 확인
        for next in graph[now]:
            next_node = next[0]
            cost = next[1]
            # next_node로 가기 위한 누적거리
            new_cost = dist + cost
            # 누적거리가 기존보다 크네?
            if distance[next_node] <= new_cost: continue
            distance[next_node] = new_cost
            heapq.heappush(pq,(new_cost,next_node))


dijkstra(0)
print(graph)
print(distance)
