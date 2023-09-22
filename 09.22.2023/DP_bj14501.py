# 퇴사 문제
# 오늘부터 N+1되는 날에 퇴사
# 남은 N일의 기간동안 최대한 많은 돈을 벌고 싶다
# 일정: 하루에 하나씩 잡아놨다
# 걸리는 기간T와 상담건당페이 P
# 퇴사날부터는 상담할 수 없기에 조심
# 알고리즘

# 지훈이 코드
days = int(input())  # 상담 날
counsel = [list(map(int, input().split())) for _ in range(days)]  # 일 돈

ans_list = [0 for _ in range(days + 1)]

for i in range(days): # 각 날을 순회합니다.
    for j in range(i + counsel[i][0], days + 1):  # 그 날에 걸리는 상담 시간 그 뒤를 순회
        if ans_list[j] < ans_list[i] + counsel[i][1]:  # i의 최대 수익 + 그 날의 상담 수익이 j의 최대 수익을 넘으면
            ans_list[j] = ans_list[i] + counsel[i][1]  # j 의 최대 수익에 그 값을 넣어라

print(max(ans_list))