N=int(input())
arr=list(map(int,input().split()))
max_peri=0
X=0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if arr[i]+arr[j]>arr[k] and arr[j]+arr[k]>arr[i] and arr[k]+arr[i]>arr[j]:
                X=arr[i]+arr[j]+arr[k]
                max_peri=max(max_peri,X)
if max_peri>0:
    print(max_peri)
else:
    print(-1)
