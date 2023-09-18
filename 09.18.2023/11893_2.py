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



flag = 1
cnt = 0
N,M = map(int,input().split())  # A갯수, B갯수
A = list(map(int,input().split()))
B = list(map(int,input().split()))
for i in range(M):
    binary_search(A,0,N-1,B[i])
print(f'# {cnt}')
'''
10 1
1 2 3 4 5 6 7 8 9 10
10
'''