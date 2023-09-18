# arr = [69, 30, 10, 2, 16, 8, 32, 21]
# N = len(arr)

def quick_sort(s, e):
    if s >= e: return
    # 피봇을 기준으로 분할 위치 찾기
    i, j = s, e
    while i <= j:
        # 피봇보다 큰 값 찾기
        while i <= e and arr[i] <= arr[s]:
            i += 1
            # i가 지나온 곳은 다 피벗보다 작은 값
        # 피봇보다 작은 값 찾기
        while arr[j] > arr[s]:
            j -= 1
            # j가 지나온 곳은 다 피벗보다 큰 값
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    # 피봇이랑 교환
    arr[s], arr[j] = arr[j], arr[s]

    quick_sort(s, j - 1)   # 왼쪽
    quick_sort(j + 1, e)   # 오른쪽


for tc in range(1, int(input())+1):
    N = int(input())  # 정수의 갯수
    arr = list(map(int,input().split()))

    # print(arr)
    quick_sort(0, N-1)
    print(f'#{tc} {arr[N//2]}')