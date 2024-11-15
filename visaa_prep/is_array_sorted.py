n=int(input())
arr=list(map(int,input().split()))
x=sorted(arr)
if arr==x:
    print("true")
else:
    print("false")
