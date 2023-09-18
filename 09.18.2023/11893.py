def binary_search(arr, lo, hi, key):
    global flag, cnt
    if lo > hi:
        return -1

    mid = (lo + hi) //2

    if arr[mid] == key:
        cnt += 1
        return mid

    elif arr[mid] > key:
        flag *= -1
        if flag == 1: return
        return binary_search(arr, lo, mid - 1, key)
    else:
        flag *= 1
        if lo != 0 and flag == 1: return
        return binary_search(arr, mid + 1, hi, key)


# arr = [1,2,3]
# N = len(arr)
# print(binary_search(arr, 0, N - 1, 4))
for tc in range(1,int(input())+1):
    flag = 1
    cnt = 0
    N,M = map(int,input().split())  # A갯수, B갯수
    A = list(map(int,input().split()))
    A.sort()
    B = list(map(int,input().split()))
    for i in range(M):
        binary_search(A,0,N-1,B[i])
    print(f'#{tc} {cnt}')