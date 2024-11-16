N=int(input())
arr=list(map(int,input().split()))
a=set()
x=[]
for i in arr:
    if i not in a:
        x.append(i)
        a.add(i)
print(*x)
