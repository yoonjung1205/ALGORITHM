N = int(input())

area = [list(map(int,input().split())) for _ in range(6)]

max_x = 0
max_y = 0
for i in range(6):
    if area[i][0] == 1 or area[i][0] == 2:
        if area[i][1] > max_x:
            max_x = area[i][1]
            max_x_idx = i
    else:
        if area[i][1] > max_y:
            max_y = area[i][1]
            max_y_idx = i


h = abs(area[(max_x_idx+1)%6][1] - area[(max_x_idx-1)%6][1])
w = abs(area[(max_y_idx+1)%6][1] - area[(max_y_idx-1)%6][1])

result = (max_x * max_y) - (h*w)
print(result * N)