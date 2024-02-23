n = int(input())

matrix = [[0,1],[1,1]]
def matrixConvolution(m1,m2) :
    newMatrix = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            s = 0
            for k in range(2):
                s += (m1[i][k] % 1e6) * (m2[k][j] % 1e6) 
            newMatrix[i][j] = s % 1e6
    return newMatrix

def getDnC(n):
    if n == 1 : return matrix
    if n % 2 :
        return matrixConvolution(matrix, getDnC(n-1))
    else :
        before = getDnC(n//2)
        return matrixConvolution(before, before)

print(int(getDnC(n)[0][1]))