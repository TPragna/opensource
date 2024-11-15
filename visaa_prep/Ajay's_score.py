N=int(input())
arr=[]
for i in range(N):
    X,Y=map(int,input().split())
    Z=X//10
    test_cases=Z*Y
    arr.append(test_cases)
for i in arr:
    print(i)
