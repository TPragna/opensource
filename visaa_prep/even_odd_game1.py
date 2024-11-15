N=int(input())
sum=0
while(N!=0):
    r=N%10
    sum+=r
    N//=10
if sum%2==0:
    print("Vignesh")
else:
    print("Charan")
