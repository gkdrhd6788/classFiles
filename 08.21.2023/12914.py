def preorder(v):
    global count
    if v : #(if  v != 0)
        count += 1
        preorder(ch1[v])
        preorder(ch2[v])
    return count

for tc in range(1,int(input())+1):
    E, N = map(int,input().split()) # E 간선의 갯수, N 서브트리의 루트
    arr = list(map(int,input().split()))

    ch1 = [0]*(E+2)
    ch2 = [0]*(E+2)
    count = 0
    for i in range(E): # 0,1,2,3,4
        p,c = arr[i*2],arr[i*2+1]
        if ch1[p] == 0:
            ch1[p]=c
        else:
            ch2[p]=c

    print(f'#{tc} {preorder(N)}')