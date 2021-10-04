n = int(input())

h = list(map(int, input().split()))
a = list(map(int, input().split()))

total = sum(h)
a.sort()
for i in range(n):
    total += i * a[i]

print(total)

    