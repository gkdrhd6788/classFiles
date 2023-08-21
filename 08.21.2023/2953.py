winner_score = 0
winner_index = 0
for index in range(1,6):
    scr1,scr2,scr3,scr4 = map(int,input().split())
    total = scr1+ scr2+scr3+scr4
    if winner_score < total:
        winner_score = total
        winner_index = index
print(winner_index, winner_score)

