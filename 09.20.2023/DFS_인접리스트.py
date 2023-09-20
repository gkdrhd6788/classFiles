# 인접리스트

graph = [
    [1, 3],
    [0,2,3,4],
    [1],
    [0,1,4],
    [1,3]
]
# (추가) 파이썬은 딕셔너리로도 구현할 수 있다. 텍스트도 가능

def dfs_stack(start):
    visited = []
    stack = [start]

    while stack:
        now = stack.pop()
        # 이미 방문한 지점이라면 continue
        if now in visited:
            continue
        # 방문하지 않은 지점이라면, 방문 표시
        visited.append(now)

        # 갈 수 있는 곳들을 stack에 추가
        for to in range(len(graph[now])-1,-1,-1):  # 역순으로 하면 작은번호부터 조회 가능
            # # 이제 연결이 안되어있다는 건 애초에 저장하지 않았으므로 체크할 필요 없음
            # if graph[now][next] == 0:
            #     continue

            next = graph[now][to]
            # 방문한 지점이라면 stack에 추가 하지 않음
            if next in visited:
                continue

            stack.append(next)

        # 출력을 위한 반환
        return visited


print("dfs_stack = ", end=' ')
print(*dfs_stack(0))

# DFS - 재귀
# MAP 크기(길이)를 알 때 append 형식 말고 아래와 같이 사용하면 훨씬 빠르다.
visited = [0] * 5
path = []  # 방문 순서 기록


def dfs(now):
    # 기저 조건

    # 들어가기 전
    visited[now] = 1  # 현재 지점 방문 표시
    print(now, end=' ')
    # 인접한 노드들을 방문
    for to in range(len(graph[now])):
        next = graph[now][to]
        if visited[next]:
            continue
        # 함수 호출
        dfs(next)
    # 돌아와서


print('dfs 재귀=', end=' ')
dfs(0)