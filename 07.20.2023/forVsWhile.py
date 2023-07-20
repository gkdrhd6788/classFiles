arr=[1,2,3]
SUM = 0

# for 문으로

for val in arr:
    SUM += val
    val = 100
print(SUM,sum(arr))  #안에서 val지정하면??


'''
#while문으로 
i = 0
while i < len(arr):
    SUM += arr[i]
    i += 1

print(SUM,sum(arr))
'''