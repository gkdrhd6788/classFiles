from pprint import pprint
from collections import deque

def BFS(M,N):
    while deq: # 큐가 비어있지 않은 경우
        i,j = deq.popleft()
        for di,dj in [[-1,0],[1,0],[0,1],[0,-1]]:
            ii , jj = i + di,j + dj
            if ii<0 or ii>N-1 or jj<0 or jj>M-1: continue
            if tomato_arr[ii][jj] == 0: # 익지않은 토마토가 있고(0) 방문하지 않은 곳이라면
                deq.append((ii,jj))
                tomato_arr[ii][jj] = tomato_arr[i][j]+1

def finding_result():
    result = 0
    for i in range(N):
        for j in range(M):
            if tomato_arr[i][j] == 0:
                return -1
            result = max(result,tomato_arr[i][j])
    return result-1

M,N = map(int,input().split()) # M가로칸, N세로칸
tomato_arr = [list(map(int,input().split())) for _ in range(N)]
# visited = [[0]*M for _ in range(N)]
deq = deque()
for n in range(N):
    for m in range(M):
        if tomato_arr[n][m] ==  1:
            deq.append((n,m)) # [(0, 0), (3, 5)]
            # visited[n][m] = 1
BFS(M,N)

print(finding_result())