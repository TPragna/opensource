N=int(input())
k=int(input())
i=str(0*k)+bin(N)[2:]
if len(i)>=k and i[-k]=='1':
    print("true")
else:
    print("false")
