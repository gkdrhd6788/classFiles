A = list(map(int,input().split()))
M = A[0]    #주어지는 숫자 수
N = A[1]    #합산해야 하는 숫자 수

num_list= list(map(int,input().split()))

max_total= min_total= 0 # (-)가 나왔을 때 대비 N을 활용해서 할 수 있는 방법

for i in range(0,(M-1)-(N-1)+1):
    each_total = 0
    print ('i',i)
    for j in range(i,i+N-1):
        print('j',j)
        each_total += A[j] #중간에서 퍼지는게 아니라 처음부터
        print(each_total)
    if each_total > max_total:
        max_total = each_total
    if each_total < min_total:
        min_total = each_total

print(max_total,min_total)