arr=[-1,3,-9,6,7,-6,1,5,4,-2]

'''def comb(cur,total):
    global ans
    if len(c)>0 and total == 0:
        print(*c)
        ans += 1
        return
    if cur == len(arr):
        return
    c.append(arr[cur])
    comb(cur+1,total+arr[cur])
    c.pop()
    comb(cur+1,total)


c = []
ans = 1
print(0)
comb(0,0)

print(ans)'''

# def partition(a,l,r):
#     p = a[l]
#     i = l
#     j = r
#     while i<=j:
#         while i<=j and a[i] <= p: # 피벗 보다 큰값을 만날때 까지 반복
#             i += 1

#         while i<=j and a[j] >= p: # 피벗보다 작은 값을 만날때 까지 반복
#             j -= 1
#         if i < j: a[i],a[j] = a[j],a[i]

#     a[l],a[j] = a[j],a[l]
#     return j

# def partition(a,l,r):
#     p = a[r]
#     i = l-1
#     for j in range(l,r):
#         if a[j] <= p:
#             i += 1
#             a[i],a[j] = a[j],a[i]
#     a[i+1],a[r] = a[r],a[i+1]
#     return i+1

# def quick_sort(a,l,r):
#     if l<r:
#         s = partition(a,l,r)
#         quick_sort(a,l,s-1)
#         quick_sort(a,s+1,r)

# print(*arr)
# quick_sort(arr,0,len(arr)-1)
# print(*arr)

# arr = [1,2,3]
# def powerset(cur,cnt):
#     if cur == len(arr):
#         print(*c)
#         return
#     if cnt == len(arr):
#         return
#     c.append(arr[cur])
#     powerset(cur+1,cnt+1)
#     c.pop()
#     powerset(cur+1,cnt)
    

# c = []    
# d=[]
# powerset(0,0)
# print(d)

map = [[0,1,1,1,0],[0,0,0,1,0],[0,1,1,1,0],[0,0,0,0,0]]
visit = [[0]*5 for _ in range(4)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]
def bfs(x,y):
    visit[x][y] = 1
    q = []
    q.append([x,y])
    while q:
        x,y = q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 4 and 0<= ny < 5 and not visit[nx][ny] and map[nx][ny] == 0:
                q.append([nx,ny])
                visit[nx][ny] = visit[x][y] + 1
bfs(0,0)
print(visit)
