def search(arr, key):
    l = 0
    h = len(arr) - 1

    while l <= h:
        mid = (l + h) // 2
        if arr[mid] == key:
            return 1
        elif arr[mid] < key:
            l = mid + 1
        else:
            h = mid - 1

    return 0


T = int(input())


for tc in range(T):
    N = int(input())
    note1 = list(map(int, input().split()))
    M = int(input())
    note2 = list(map(int, input().split()))
    note1.sort()

    for num in note2:
        print(search(note1,num))

