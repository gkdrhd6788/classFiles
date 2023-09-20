
def dfs(now,total,cnt):
    global min_cnt
    global M
    if min_cnt < cnt :return
    if total > M: return
    if total== M:
        min_cnt = cnt
        return

    visited[now] = 1  # 현재 지점 방문 표시
    # print(now, end=' ')
    # 인접한 노드들을 방문
    for to in range(len(graph[now])):
        next = graph[now][to]
        if visited[next]:
            continue
        # 함수 호출
        if next %4==0:
            dfs(next,total-10,cnt+1)
        elif next %4==1:
            dfs(next,total+1,cnt+1)
        elif next %4==2:
            dfs(next,total-1,cnt+1)
        else:
            dfs(next,total*2,cnt+1)
    # 돌아와서
