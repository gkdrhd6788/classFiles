def merge_sort(lo, hi): # 구간 정보 (시작, 끝)
    global cnt
    if lo == hi: return
    mid = (lo + hi) // 2
    merge_sort(lo, mid)
    merge_sort(mid + 1, hi)
    # 병합
    i, j, k = lo, mid + 1, lo

    while i <= mid and j <= hi:
        if arr[i] < arr[j]:
            tmp[k] = arr[i]; i += 1; k += 1
        else:
            tmp[k] = arr[j]; j += 1; k += 1
    while i <= mid:
        tmp[k] = arr[i]; i += 1; k += 1
    while j <= hi:
        tmp[k] = arr[j]; j += 1; k += 1

    for i in range(lo, hi + 1):
        arr[i] = tmp[i]

cnt = 0
N = int(input())
arr = list(map(int,input().split()))
tmp = [0] * len(arr)
merge_sort(0, len(arr) - 1)
print(arr[N//2],cnt)
