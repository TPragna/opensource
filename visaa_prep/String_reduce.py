N=input()
S=""
count=1
for i in range(1,len(N)):
    if(N[i]==N[i-1]):
        count+=1
    else:
        S+=N[i-1]+str(count)
        count=1
S+=N[-1]+str(count)
print(S)
