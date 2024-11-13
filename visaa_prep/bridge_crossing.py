x,y,z=map(int,input().split())
sum=y
c=0
while(sum+x<=z):
    sum+=x
    c+=1
print(c)
