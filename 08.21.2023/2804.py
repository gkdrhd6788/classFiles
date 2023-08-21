A , B = input().split()  # A는 가로 B는 세로
found = False
for i in range(len(A)):
    for j in range(len(B)):
        if A[i] == B[j]:
            found= True
            break
    if found:
        break
# A에서 공통자리, B에서 공통자리
Acommon, Bcommon = i,j

for i in range(len(B)):
    if i != Bcommon:
        print('.'*Acommon,end='')
        print(B[i], end = '')
        last= len(A)-(Acommon+1)
        print('.'*last)
    else:
        print(A)
