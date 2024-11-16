N=int(input())
arr=list(map(int,input().split()))
count=0
max_con=0
for i in range(N):
    if arr[i]==0:
        count+=1
    else:
        max_con=max(max_con,count)
        count=0
print(max_con)
