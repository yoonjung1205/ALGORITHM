m, total = map(int,input().split())
card = list(map(int,input().split()))

arr = []
sum_list=[]
def recur(cnt,cur):
    if cnt == 3:
        arr_sum = sum(arr)
        if arr_sum <= total:
            sum_list.append(arr_sum)
        return

    if cur == m+1:
        return

    arr.append(card[cur-1])
    recur(cnt+1,cur+1)
    arr.pop()
    recur(cnt,cur+1)

recur(0,1)
print(max(sum_list))
