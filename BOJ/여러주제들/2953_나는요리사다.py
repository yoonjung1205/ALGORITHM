total = [0]*6

for i in range(1,6):
    tmp = list(map(int,input().split()))
    total[i] = sum(tmp)

print(total.index(max(total)), max(total))