from collections import deque

def BFS(s): # s 시작정점 n 정점의 갯수
    deq.append(s)
    visited[s] = 1
    while deq:
        next = deq.popleft()
        print(next,end=' ')
        for i in adj[next]:
            if visited[i] != 0: continue
            deq.append(i)
            visited[i] = 1

def DFS(s):
    visited2[s]=1
    print(s,end=' ')
    for i in adj[s]:
        if visited2[i] != 0 : continue
        DFS(i)



N,M,V = map(int,input().split())  #정점의 개수, 간선의 개수, 시작정점
adj = [[] for _ in range(N+1)]
for _ in range(M):
    q,w = map(int,input().split())
    adj[q].append(w)
    adj[w].append(q)

for lst in adj:
    lst.sort()

deq = deque()
visited = [0]*(N+1)
visited2 = [0]*(N+1)

DFS(V)
print()
BFS(V)


