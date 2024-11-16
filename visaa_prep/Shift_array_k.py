N=int(input())
arr=list(map(int,input().split()))
K=int(input())
K=K%N
X=arr[-K:]+arr[:-K]
print(*X)
