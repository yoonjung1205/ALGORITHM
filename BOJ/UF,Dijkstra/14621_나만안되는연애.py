def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

def union(x,y):
    x=find(x)
    y=find(y)

    if rank[x] > rank[y]:
        parent[y] = x
    elif rank[x] < rank[y]:
        parent[x] = y
    else:
        parent[y] = x
        rank[x] += 1


# N: 학교 수, M: 도로의 수
N, M = map(int,input().split())
univ = [0]+list(map(str,input().split()))
# print(univ)

temp = []
for i in range(M):
    s,e,w = map(int,input().split())
    temp.append([s,e,w])
temp.sort(key= lambda x:x[2])
# print(temp)

parent = list(range(N+1))
# print(parent)

rank = [0] * (N+1)
ans = 0
cnt = 0
for t in temp:
    x = t[0]
    y = t[1]
    w = t[2]
    if find(x) == find(y): # cycle 생기는 경우
        continue
    if univ[x] == univ[y]: # 같은 대학인 경우(남남 or 여여)
        continue
    ans += w
    cnt += 1    # UF을 수행한 횟수 카운트
    union(x,y)

if cnt + 1 != N:    # 실제 노드 개수 == UF 횟수보다 1 크니까!
    print(-1)
else:
    print(ans)