input_list = list(map(int,input().split()))
i = min(input_list)

while True:
    cnt = 0        
    for j in range(5):
        if i % input_list[j] == 0:
            cnt += 1
    if cnt >=3:
        print(i)
        break
    i += 1
                
