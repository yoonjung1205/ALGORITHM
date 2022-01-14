'''
5 3 20
10 10 20 20 30
1 3
2 4
5 4

5 3 10
10 10 20 20 30
1 3
2 4
5 4
'''

# 33퍼에서 오류 해결~~ 한번더 find할 때 잘못함 ㅠㅠ
def find(x):
    if parent[x] == x:
        return x
    else:
        return find(parent[x])

def union(x,y):
    x = find(x)
    y = find(y)

    if rank[x] < rank[y]:
        parent[x] = y
    elif rank[x] > rank[y]:
        parent[y] = x
    else:
        parent[x] = y
        rank[y] += 1


N,M,k = map(int, input().split())
A = [0]+list(map(int, input().split()))

parent = list(range(N+1))
rank = [0] * (N+1)
for _ in range(M):
    v,w = map(int,input().split())
    if find(v) != find(w):  # 부모가 같으면 굳이 해줄 필요가 없어서
        union(v,w)

print('parent: ',parent)
print('rank: ',rank)

# 혹시나 루트노드를 못 찾았을 경우를 대비해서 한 번더 find
for i in range(len(parent)):
    parent[i] = find(parent[i])

ans = 0
money = [[] for _ in range(10001)]
for i in range(len(parent)):
    money[parent[i]].append(A[i])   # money[3] = [10,20], money[4] = [10,20,30]
print(money)
for i in range(len(money)):
    if money[i]:
        ans += min(money[i])

if ans > k:
    print('Oh no')
else:
    print(ans)