N,X,Y=map(int,input().split()) 
marks=N*X
if(0<=Y<=marks and Y%X==0):
    print("YES")
else:
    print("NO")
