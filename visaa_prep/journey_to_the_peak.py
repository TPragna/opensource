n=int(input())
arr=list(map(int,input().split()))
alt=0
max_alt=0
for i in arr:
    alt+=i
    max_alt=max(max_alt,alt)
print(max_alt)
    
