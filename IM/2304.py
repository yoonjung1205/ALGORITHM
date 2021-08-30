N = int(input())

stick = [list(map(int,input().split())) for _ in range(N)]
stick.sort()

# x = 2 3 4 5 6 7 8  9 10 11 12 13 14 15
# y = 4   6       10                  8
#                 (max) 

max_y = 0
for i in range(N):
    if stick[i][1] > max_y:
        max_y = stick[i][1]
        max_y_x = stick[i][0]


stick_list = [0] * (stick[-1][0]+1)
for x,y in stick:
    stick_list[x] = y

temp = 0
total = 0
for i in range(max_y_x + 1):
    if stick_list[i] > temp:
        temp = stick_list[i]
    total += temp

temp = 0
for i in range(stick[-1][0],max_y_x,-1):
    if stick_list[i] > temp:
        temp = stick_list[i]
    total += temp
print(total)

# 참고 : https://namhandong.tistory.com/138


    

    






