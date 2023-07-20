result = ['a','b','c']
#print(list(enumerate(result))) #튜플로 나옴(인덱스,요소) [(0, 'a'), (1, 'b'), (2, 'c')] 

for index, elem in enumerate(result):  # 따라서 이게 가능
    print(index,elem)

#enumerate(iterable, start = 0) #default값이 start = 0 임


# enumerate는 range ( len ( ) ) 을 대체할 수 있음
for i in range(len(result)):
    print(i, result[i])
