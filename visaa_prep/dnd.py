n,m=map(int,input().split())
arr=list(map(int,input().split()))
x=0
y=0
for i in arr:
    if i%m==0:
        x+=i
    else:
        y+=i
print(x-y)
