import heapq
def dijkstra(si,sj):
    pq = []
    heapq.heappush(pq,(0,si,sj))
    distance[si][sj] = 0
    while pq:
        dist,ni,nj = heapq.heappop(pq)
        if distance[ni][nj] < dist: continue
        for di,dj in [[1,0],[0,1],[-1,0],[0,-1]]:
            ii,jj= ni+di,nj+dj
            if ii<0 or jj<0 or ii>N-1 or jj> N-1: continue
            if arr[ii][jj] > arr[ni][nj]:
                new_cost = dist + 1 + ( arr[ii][jj] - arr[ni][nj] )
            else:
                new_cost = dist + 1
            if distance[ii][jj] <= new_cost: continue
            distance[ii][jj] = new_cost
            heapq.heappush(pq,(new_cost,ii,jj))


for tc in range(1,int(input())+1):
    N = int(input()) # 가로세로크기
    arr = [list(map(int,input().split())) for _ in range(N)]
    distance = [[int(1e9)]*N for _ in range(N)]
    dijkstra(0,0)
    print(f'#{tc} {distance[N-1][N-1]}')

