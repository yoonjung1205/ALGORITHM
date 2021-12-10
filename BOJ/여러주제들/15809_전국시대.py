N, M = map(int,input().split())

army = [0] + [int(input()) for _ in range(N)]

info = [list(map(int,input().split())) for _ in range(M)]

# opq, o:1(pq 동맹), o:2(pq 전쟁)
# print('before: ',army)
# print(info)

parent = list(range(len(army)))
rank = [0 for _ in range(len(army))]

def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)

    if rank[x] > rank[y]:
        parent[y] = x

    elif rank[x] < rank[y]:
        parent[x] = y
    else:
        parent[x] = y
        rank[y] += 1

for i in range(M):
    # 동맹(앞쪽으로 union)
    if info[i][0] == 1:
        army[parent[info[i][1]]] = army[info[i][1]] + army[info[i][2]]
        army[parent[info[i][2]]] = 0
        union(info[i][2], info[i][1])
        print('alliance: ',army)
        print(parent)

    # 전쟁(값이 큰쪽으로 union)
    else:
        if army[parent[info[i][1]]] < army[parent[info[i][2]]]:
            army[parent[info[i][2]]] = abs(army[parent[info[i][1]]] - army[parent[info[i][2]]])
            army[parent[info[i][1]]] = 0
            union(info[i][1], info[i][2])

        elif army[parent[info[i][1]]] > army[parent[info[i][2]]]:
            army[parent[info[i][1]]] = abs(army[parent[info[i][1]]] - army[parent[info[i][2]]])
            army[parent[info[i][2]]] = 0
            union(info[i][2], info[i][1])

        else:
            army[parent[info[i][1]]] = 0
            army[parent[info[i][2]]] = 0

        print('fight: ',army)
        print(parent)
        print(rank)

for i in range(len(parent)):
    find(i)



army = list(set(army))[1:]
army.sort()
ans = []
for i in army:
    if i:
        ans.append(i)
print(*ans)