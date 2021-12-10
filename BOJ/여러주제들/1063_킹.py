# R : 한 칸 오른쪽으로(열 +1)
# L : 한 칸 왼쪽으로(열 -1)
# B : 한 칸 아래로(행 -1)
# T : 한 칸 위로(행 +1)
# RT : 오른쪽 위 대각선으로(+1,+1)
# LT : 왼쪽 위 대각선으로(+1,-1)
# RB : 오른쪽 아래 대각선으로(-1,+1)
# LB : 왼쪽 아래 대각선으로(-1,-1)

king, stone, N = map(str,input().split())
N = int(N)

move_list = [input() for _ in range(N)]

position = {'A':1,
            'B':2,
            'C':3,
            'D':4,
            'E':5,
            'F':6,
            'G':7,
            'H':8,}
re_position = dict(map(reversed, position.items()))
# print(re_position)

king = [int(king[1]), position[king[0]]]    # x: 열, y: 행
stone = [int(stone[1]), position[stone[0]]]

for m in move_list:
    kx = king[0]
    ky = king[1]
    sx = stone[0]
    sy = stone[1]
    if m == 'R':
        nky = ky + 1
        nsy = sy + 1
        if 0 < nky < 9:
            if kx == sx and nky == sy:
                if 0 >= nsy or nsy >= 9:
                    continue
                stone[1] = nsy
            king[1] = nky
    elif m == 'L':
        nky = ky - 1
        nsy = sy - 1
        if 0 < nky < 9:
            if kx == sx and nky == sy:
                if 0 >= nsy or nsy >= 9:
                    continue
                stone[1] = nsy
            king[1] = nky
    elif m == 'B':
        nkx = kx - 1
        nsx = sx - 1
        if 0 < nkx < 9:
            if nkx == sx and ky == sy:
                if 0 >= nsx or nsx >= 9:
                    continue
                stone[0] = nsx
            king[0] = nkx
    elif m == 'T':
        nkx = kx + 1
        nsx = sx + 1
        if 0 < nkx < 9:
            if nkx == sx and ky == sy:
                if 0 >= nsx or nsx >= 9:
                    continue
                stone[0] = nsx
            king[0] = nkx
    elif m == 'RT':
        nkx = kx + 1
        nsx = sx + 1
        nky = ky + 1
        nsy = sy + 1
        if 0 < nkx < 9 and 0 < nky < 9:
            if nkx == sx and nky == sy:
                if (0 >= nsx or nsx >= 9) or (0 >= nsy or nsy >= 9):
                    continue
                stone[0] = nsx
                stone[1] = nsy
            king[0] = nkx
            king[1] = nky
    elif m == 'LT':
        nkx = kx + 1
        nsx = sx + 1
        nky = ky - 1
        nsy = sy - 1
        if 0 < nkx < 9 and 0 < nky < 9:
            if nkx == sx and nky == sy:
                if (0 >= nsx or nsx >= 9) or (0 >= nsy or nsy >= 9):
                    continue
                stone[0] = nsx
                stone[1] = nsy
            king[0] = nkx
            king[1] = nky
    elif m == 'RB':
        nkx = kx - 1
        nsx = sx - 1
        nky = ky + 1
        nsy = sy + 1
        if 0 < nkx < 9 and 0 < nky < 9:
            if nkx == sx and nky == sy:
                if (0 >= nsx or nsx >= 9) or (0 >= nsy or nsy >= 9):
                    continue
                stone[0] = nsx
                stone[1] = nsy
            king[0] = nkx
            king[1] = nky
    elif m == 'LB':
        nkx = kx - 1
        nsx = sx - 1
        nky = ky - 1
        nsy = sy - 1
        if 0 < nkx < 9 and 0 < nky < 9:
            if nkx == sx and nky == sy:
                if (0 >= nsx or nsx >=9) or (0 >= nsy or nsy >= 9):
                    continue
                stone[0] = nsx
                stone[1] = nsy
            king[0] = nkx
            king[1] = nky


print(re_position[king[1]]+str(king[0]))
print(re_position[stone[1]]+str(stone[0]))