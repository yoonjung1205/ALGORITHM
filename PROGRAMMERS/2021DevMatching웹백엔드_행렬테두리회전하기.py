def solution(rows, columns, queries):
    answer = []
    matrix = [[0]*(columns+1) for _ in range(rows+1)]
    print(matrix)

    for i in range(1,rows+1):
        for j in range(1,columns+1):
            matrix[i][j] = ((i-1)*columns + j)

    for num in range(len(queries)):
        matrix[queries[num]][]

    print(matrix)
    return answer



solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]])