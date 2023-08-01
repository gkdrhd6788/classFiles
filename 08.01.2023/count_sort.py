def counting_sort(A,B,k):
# A [] -- 입력 배열
# B [] -- 정렬된 배열
# C [] -- 카운트 배열
    C = [0] * (k+1)  # 0부터 k까지이므로 k+1개의 칸이 필요

    for i in range(0,len(A)):   #각 숫자의 갯수 카운팅하기
        C[A[i]] += 1    # A[0]~A[n] 값이 C카운트 배열의 index가 된다.

    for i in range(1, len(C)):  #각 숫자까지의 카운팅 누적
        C[i] = C[i]+ C[i-1]     # i-1 =0 부터 시작되야 하므로 위에 range시작값이 1

    for i in range(len(A)-1,-1,-1):  # 거꾸로 탐색
        C[A[i]] = C[A[i]] - 1        # 각 숫자의 카운팅 누적 값을 B의 index로 설정해주기 위함
        B[C[A[i]]]= A[i]             # 입력 배열 값을 각 숫자의 뒤에서 부터 저장

    return B

A=[0,4,1,3,1,2,4,1]
B=[0]*len(A)
k=4
print(counting_sort(A,B,k))