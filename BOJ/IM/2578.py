bingo = [list(map(int,input().split())) for _ in range(5)]
call = [list(map(int,input().split())) for _ in range(5)]

new_call = []
for i in range(5):
    for j in range(5):
        new_call.append(call[i][j])

cnt = 0
row = [0]*5
col = [0]*5
daegak1 = 0
daegak2 = 0
for k in range(len(new_call)):
    if cnt == 3:
        break
    for i in range(len(bingo)):
        if cnt == 3:
            break
        for j in range(len(bingo[i])):
            if cnt == 3:
                break
            if new_call[k] == bingo[i][j]:
                bingo[i][j] = 0
                row[i] += 1
                col[j] += 1
                
                if i == j:
                    daegak1 += 1
                if i == 4-j:
                    daegak2 += 1

                for r in range(5):
                    if row[r] == 5:
                        row[r] = 0
                        cnt += 1
                        if cnt == 3:
                            break
                    if col[r] == 5:    
                        col[r] = 0
                        cnt += 1
                        if cnt == 3:
                            break
                    if daegak1 == 5:
                        daegak1 = 0
                        cnt += 1
                        if cnt == 3:
                            break
                    if daegak2 == 5:
                        daegak2 = 0
                        cnt += 1
                        if cnt == 3:
                            break
                        
                        
              
print(k)

'''
# 출처 : https://velog.io/@jajubal/파이썬백준-2578-빙고
bingo = []
for _ in range(5):
    bingo.append(list(map(int, input().split())))

num = list(map(int, input().split()))
for _ in range(4):
    num += list(map(int, input().split()))

check = [0] * 12 #바뀐것의 갯수 저장하는 리스트 idx0~4는 row / 5~9는 col / 10, 11은 대각
line = 0
flag = False
for n in range(25): #사회자가 하나씩 부른다.
    if flag == True:
        break
    for i in range(5): #빙고탐색
        if flag == True:
            break
        for j in range(5):
            if flag == True:
                break
            if num[n] == bingo[i][j]: #사회자가 부른거 찾으면
                bingo[i][j] = 0 #0 으로 바꾸고
                check[i] += 1 #행 바뀐거 체크
                check[j+5] += 1 #열 바뀐거 체크
                if i == j: #대각
                    check[10] += 1
                if i + j == 4: #반대대각
                    check[11] += 1
                for c in range(12): #바뀐것 갯수 저장하는 리스트 탐색해서
                    if check[c] == 5: #5번 바뀌었으면
                        check[c] = 0 # 초기화시키고
                        line += 1 #빙고처리
                        if line == 3:
                            flag = True
                            break
print(n)

'''