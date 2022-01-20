def solution(rows, columns, queries):
    answer = []
    matrix = [[0]*(columns+1) for _ in range(rows+1)]

    print(matrix)

    for i in range(1,rows+1):
        for j in range(1,columns+1):
            matrix[i][j] = ((i-1)*columns + j)


    for query in queries:
        r1 = query[0]
        c1 = query[1]
        r2 = query[2]
        c2 = query[3]
        p = matrix[r1][c2]
        for i in range(c2,c1,-1):
            tmp = matrix[r1][i-1]
            matrix[r1][i] = tmp
        for i in range(r2,r1+1,-1):
            tmp = matrix[i-1][c2]
            matrix[i][c2] = tmp
        matrix[r1+1][c2] = p

    print(matrix)
    return answer



solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]])