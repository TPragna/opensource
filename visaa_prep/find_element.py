n=int(input())
arr=list(map(int,input().split()))
k=int(input())
x=0
y=n-1
z=-1
while(x<=y):
    mid=(x+y)//2
    if arr[mid]==k:
        z=mid
        break
    elif k>arr[mid]:
        x=mid+1
    else:
        y=mid-1
print(z)
