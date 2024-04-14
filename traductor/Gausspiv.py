import pivpar
import pivtot
import sustreg

def GaussPiv(A, b, n, Piv):
    """
    Calcula la solución de un sistema de ecuaciones Ax=b, ya sea
    sin pivoteo piv=0, usando pivoteo parcial piv=1 o pivoteo total piv=2. 
    Donde A es de tamaño nxn y b de tamaño nx1
    """
    Ab = [A[i] + [b[i]] for i in range(n)]
    mark = list(range(n))
    for k in range(n-1):
        if Piv == 1:
            Ab = pivpar.pivpar(Ab, n, k)
        elif Piv == 2:
            Ab, mark = pivtot.pivtot(Ab, mark, n, k)
        for i in range(k+1, n):
            M = Ab[i][k] / Ab[k][k]
            for j in range(k, n+1):
                Ab[i][j] -= M * Ab[k][j]
    x = sustreg.sustreg(Ab, n)
    print('x:', x, 'mark:', mark)
    return x, mark

GaussPiv([[4, 3, -2,-7], [3, 12, 8,-3], [2, 3, -9,3],[1, -2, -5, 6]], [20, 18, 31, 12], 4, 1)