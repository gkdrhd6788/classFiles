

''' dict으로 풀려고 했으나, 카드 장수가 같을 때는 큰 숫자 구현이 어려웠음
for tc in range(1,T+1):
    num_of_num = int(input())
    num_list = list(map(int,input()))  #input().split()안되나?
    count_dict = {}
    for i in num_list:
        count_dict[i]=num_list.count(i)
    sorted_dict_list = sorted(count_dict.items(),key=lambda x:x[1]) #lambda 이해하기
    print(sorted_dict_list)
    print(f'#{tc} {sorted_dict_list[-1][0]} {sorted_dict_list[-1][1]} ')
    '''

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_list = list(map(int,input()))
    count_list = [0]*10
    sorted_list = [0]* N

    for i in range(0,N): #카운팅하기
        count_list[num_list[i]] += 1

    max_count = 0 # 디버그 방법 (?이 뜬 이유: 입력값이 없어서)
    max_num =0

    for i in range(10):
        if count_list[i] >= max_count:
            max_count = count_list[i]
            max_num = i


    print(f'#{tc} {max_num} {max_count}')
