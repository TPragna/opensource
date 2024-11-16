N,M=map(int,input().split())
matrix=[]
for i in range(N):
    X=list(map(int,input().split()))
    matrix.append(X)
r,c=[],[]
for i in range(N):
    for j in range(M):
        if matrix[i][j]==0:
            r.append(i)
            c.append(j)
for i in range(N):
    for j in range(M):
        if i in r or j in c:
            matrix[i][j]=0
for i in range(N):
    for j in range(M):
        print(matrix[i][j],end=" ")
    print("")
