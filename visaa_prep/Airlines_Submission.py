X,N=map(int,input().split())
Y=X*100
if(N>Y):
    Z=N-Y
    if Z%100==0:
        W=Z//100
    else:
        W=(Z//100)+1
else:
    W=0
print(W)
