N=int(input())
arr=list(map(int,input().split()))
r=arr[1:]+arr[:1]
print(*r)
