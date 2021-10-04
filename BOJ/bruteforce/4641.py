while True:
    input_list = list(map(int,input().split()))
    if -1 in input_list:
        break
    cnt = 0
    for i in range(len(input_list)-1):
        for j in range(len(input_list)-1):
            if input_list[i]/input_list[j] == 2:
                cnt += 1

    print(cnt)