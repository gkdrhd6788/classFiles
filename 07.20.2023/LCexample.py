#0~9요소 + 홀수 리스트 만들기

# 일반적인 방법
newList = []
for i in range(10):
    if i%2 == 1:
        newList.append(i)

print(newList)


#List Comprehension 사용
new_list_2 =[i for i in range(10) if i%2==1]
print(new_list_2)

new_list_3 = [i if i%2 ==1 else str(i) for i in range(10)] #else사용하면 순서가 바뀜
print(new_list_3)