N=int(input())
arr=[]
for i in range(N):
    X,Y=map(int,input().split())
    Z=X//10
    test_cases=Y*Z
    arr.append(test_cases)
for i in arr:
    print(i)
