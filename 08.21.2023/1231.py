def inorder(v):
    inorder(ch1[v])
    inorder(ch2[v])
    print(arr[v])

N = int(input()) # 정점의 갯수(1~100)
arr = [0]*(N+1) # 문자 저장
ch1=[0]*(N+1)
ch2=[0]*(N+1)


for i in range(1,N+1):
    each_array=input().split() # [1,W,2,3]  여전히 str
    if len(each_array) == 4:
        arr[i]=each_array[1]
        ch1[i]=int(each_array[2])
        ch2[i]=int(each_array[3])
    elif len(each_array) ==3:
        arr[i] = each_array[1]
        ch1[i] = int(each_array[2])
    elif len(each_array)==2:
        arr[i] = each_array[1]
# print(arr)
# print(ch1)
# print(ch2)
inorder(1)
