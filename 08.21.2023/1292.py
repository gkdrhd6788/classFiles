list = []
A,B = map(int,input().split())
for i in range(1,50):
    for j in range(i):
        list.append(i)
#print(list)
total = 0
for i in range(1,B+1): # 1 2 3 4 5 6 7
    if A <= i <= B:
        total += list[i-1]
print(total)


