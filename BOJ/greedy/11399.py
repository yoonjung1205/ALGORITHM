n = int(input())
t = list(map(int,input().split()))

for i in range(len(t)):
    for j in range(len(t)):
        if t[i] < t[j]:
            t[i],t[j] = t[j],t[i]

total = 0
sum_list = []
for i in range(len(t)):
    total += t[i]
    sum_list.append(total)

print(sum(sum_list))