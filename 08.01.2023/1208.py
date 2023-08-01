for tc in range(1,11):
    dump_max = int(input())
    num_list = list(map(int, input().split()))
    max_index = min_index = 0
    for i in range(dump_max): # 덤프 반복
        for index in range(len(num_list)): # 숫자 돌기
            if num_list[index] < num_list[min_index]:
                min_index = index
            if num_list[index] > num_list[max_index]:
                max_index = index
        num_list[max_index] -= 1
        num_list[min_index] += 1

        #주어진 덤프 횟수 이내에 평탄화 완료 대비
        if num_list[max_index]-num_list[min_index] <= 1:
            break

    for index in range(len(num_list)): # 숫자 돌기
        if num_list[index] < num_list[min_index]:
            min_index = index
        if num_list[index] > num_list[max_index]:
            max_index = index

    print(f'#{tc} {num_list[max_index]-num_list[min_index]}')
