from collections import deque

def merge_sort(lst):
    global cnt
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    l = deque()
    r = deque()
    l.extend(merge_sort(lst[:mid]))
    r.extend(merge_sort(lst[mid:]))
    # l, r은 정렬된 리스트
    ret = []
    while l and r:
        if l[0] <= r[0]:
            ret.append(l.popleft())
        else:
            ret.append(r.popleft())
    if l:
        ret.extend(l)
        cnt += 1
    if r: ret.extend(r)

    return ret  # 병합

for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int,input().split()))
    cnt = 0
    # print(arr)
    print(f'#{tc} {merge_sort(arr)[N//2]} {cnt}')