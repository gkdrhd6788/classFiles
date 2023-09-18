def binary_search_iter(arr, lo, hi, key):
    # 중간 위치 선택
    global cnt
    flag = 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == key:
            cnt += 1
            return mid
        elif arr[mid] > key:
            flag *= -1
            if flag == 1: return
            hi = mid - 1

        else:
            flag *= 1
            if flag == 1 and lo !=0: return
            lo = mid + 1
    return -1


for tc in range(1,int(input())+1):
    # flag = 1
    cnt = 0
    N,M = map(int,input().split())  # A갯수, B갯수
    A = list(map(int,input().split()))
    A.sort()
    B = list(map(int,input().split()))
    for i in range(M):
        binary_search_iter(A,0,N-1,B[i])
    print(f'#{tc} {cnt}')