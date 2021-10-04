N = int(input())

seat = input()
c_h = 1
cnt = 0
for i in range(len(seat)):
    if seat[i] == 'S':
        c_h += 1
    if seat[i] == 'L':
        cnt += 1

c_h += cnt // 2
print(min(c_h,N))


