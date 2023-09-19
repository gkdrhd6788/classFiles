arr = [i for i in range(1,4)]
path = [0]*3

def backtracking(cnt) :
    # 기저 조건
    # 숫자 3개를 골랐을 때 종료
    if cnt == 3:
        print(*path)
        return

    for num in arr:
        # 가지치기 - 중복된 숫자 제거
        if num in path:
            continue
        # 들어가기 전 로직 - 경로 저장
        path[cnt] = num
        # 다음 재귀 함수 호출
        backtracking(cnt + 1)
        # 돌아와서 할 로직(초기화)
        path[cnt] = 0

backtracking(0)