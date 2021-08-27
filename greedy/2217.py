N = int(input())
w = [int(input()) for _ in range(N)]
w.sort()
new_w = []
l = len(w)
for i in range(len(w)):
    new_w.append(w[i]*(l-i))

print(max(new_w))


