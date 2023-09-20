from collections import deque


def bfs(start):
    visited = [0]*(1000001)
    queue = deque()
    queue.append(start)
    visited[start]=1

    while queue:
        now = queue.popleft()
       #계산결과들을 큐에 추가 (자연수 only)
        cal = [now+1,now-1,now*2,now-10]
        if M in cal:
            return visited[now]
        for next in cal:
            if next <=0: continue
            if next > 1000000: continue
            if visited[next]!=0: continue # 위 2줄 범위체크 전에 두면, index error뜰 수 있음

            queue.append(next)
            visited[next] = visited[now]+1



for tc in range(1,int(input())+1):
    N,M = map(int,input().split()) #N처음 수, M 목적수
    print(f'#{tc} {bfs(N)}')
