N = int(input()) # 수열의 크기
arr = list(map(int,input().split()))
max_total = 0
total = 0

for i in range(1,N):
    if arr[i]> arr[i-1]:
        total += arr[i] - arr[i-1]
        if max_total < total :
            max_total = total
    else:
        total = 0
print(max_total)