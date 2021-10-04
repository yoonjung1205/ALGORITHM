a = [int(input()) for i in range(9)]

r = sum(a) - 100

for i in range(0,8):
    for j in range(i+1,9):
        if a[i] + a[j] == r:
            l = a[i]
            m = a[j]
a.remove(l)
a.remove(m)
a.sort()
for i in a:
    print(i)