X=int(input())
if((X%4==0)and(X%100!=0)):
    print("YES")
elif((X%400==0)and(X%100==0)):
    print("YES")
else:
    print("NO")
