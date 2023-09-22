# 격자판의 숫자 이어 붙이기
# 16자리에 10개(0에서 9까지) 숫자가 중복으로 적혀있다
# 임의의 위치에서 시작 --> i,j 모두 순회한다
# 동서남북--델타 활용
# 6번 이동--> 7자리 완성
# 다시 거쳐도 됨--> visited를 사용하지 않아도 않아도 됨
# 0으로 시작가능--> 문자열 활용 가능
# 격자판을 벗어나는 이동 안됨(범위 설정)
# 서로다른 갯수--> 중복 없애야 함(set)
# 알고리즘 : 완전 탐색 (가지치기 불가능)

def func( i, j, ans):
    if len(ans) == 7:  # 7인지 6인지 확인
        cnt_set.add(ans)
        return
    for di,dj in [[1,0],[-1,0],[0,1],[0,-1]]:
        ii,jj = i+di,j+dj
        if ii < 0 or ii > (4 - 1) or jj < 0 or jj > (4 - 1) : continue
        func( ii, jj, ans + arr[ii][jj] )



T = int(input())
arr = [input().split() for _ in range(4)]
cnt_set = set()
for i in range(4):
    for j in range(4):
        func(i,j,arr[i][j])
print(len(cnt_set))