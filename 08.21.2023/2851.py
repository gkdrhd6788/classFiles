total = 0
for _ in range(10):
    num = int(input())
    total += num
    if total >= 100 :
        break
if total-100 > 100-(total-num):
    print(total-num)
else:
    print(total)
