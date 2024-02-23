n, B = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

def matrixConvolution(m1,m2) :
    newMatrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            s = 0
            for k in range(n):
                s += (m1[i][k] * m2[k][j])
            newMatrix[i][j] = s % 1000
    return newMatrix

def getDnC(b):
    if b == 1 : return matrix
    if b % 2 :
        return matrixConvolution(matrix, getDnC(b-1))
    else :
        before = getDnC(b//2)
        return matrixConvolution(before, before)

ans = getDnC(B)
for i in range(n):
    for j in range(n):
        ans[i][j] %= 1000
for x in ans :
    print(*x)