N = int(input())
w = list(map(int,input().split()))
w.sort()
total = 0
total_list = []
for i in range(len(w)):
    total += w[i]
    total_list.append(total)
print(w)
print(total_list)