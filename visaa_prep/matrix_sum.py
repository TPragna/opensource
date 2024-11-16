N=int(input())
matrix=[]
for i in range(N):
    X=list(map(int,input().split()))
    matrix.append(X)
Y=0
for i in range(N):
    Y=sum(matrix[i])
    for j in range(N):
        Y+=matrix[j][i]
    print(Y,end=" ")
