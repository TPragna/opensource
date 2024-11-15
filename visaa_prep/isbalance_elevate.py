N=int(input())
arr=list(map(int,input().split()))
x=[]
for i in range(N):
    l=sum(arr[0:i])
    r=sum(arr[i+1:])
    d=abs(l-r)
    x.append(d)
print(*x)
