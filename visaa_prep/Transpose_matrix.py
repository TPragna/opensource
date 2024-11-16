N=int(input())
matrix=[]
for i in range(N):
    X=list(map(int,input().split()))
    matrix.append(X)
for i in range(N):
    for j in range(N):
        print(matrix[j][i],end=" ")
    print("")
