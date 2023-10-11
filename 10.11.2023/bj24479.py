import sys
sys.setrecursionlimit(10**5)
def DFS(now):
    global cnt
    cnt += 1
    visited[now] = cnt
    for to in adj[now]:
        if visited[to]:continue
        DFS(to)

# 정점의 수 N , 간선의 수 M , 시작 정점 R
N,M,R = map(int,input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    u,v = map(int,input().split())
    adj[u].append(v)
    adj[v].append(u)
for line in adj:
    line.sort()
visited = [0] * (N + 1)
cnt =0
DFS(R)
for i in visited[1:]:
    print(i)