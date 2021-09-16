N = int(input())
my_list = []
ans = []
for i in range(N):
    my_list.append(int(input()))

for i in range(N):
    for j in range(2,min(my_list)+1):
        if my_list[i] % j