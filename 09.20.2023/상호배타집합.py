# 1~10
# make set
# 각 요소가 가리키는 값이 부모
parent = [i for i in range(10)]


# find-set
def find_set(x):
    if parent[x]==x:
        return x
    #return find_set(parent[x])
    # 경로 압축
    parent[x] = find_set(parent[x])
    return parent[x]


# union
def union(x,y):
    # 1. 이미 같은 집합인지 체크
    x = find_set(x)
    y = find_set(y)
    if x==y:
        return
    # 2. 다른 집합이라면, 같은 대표자로 수정 (그냥 parent[y]=x해도 됨)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

union(0,1)
union(2,3)

# 대표자 검색
print(find_set(0))
print(find_set(1))

# 같은 그룹인지 판별
t_x = 0
t_y = 1
if find_set(t_x)==find_set(t_y):
    print(f"{t_x}와 {t_y}는 같은 그룹")
else:
    print(f"{t_x}와 {t_y}는 다른 그룹")
