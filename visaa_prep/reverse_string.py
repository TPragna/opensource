n=int(input())
x=-1 if n<0 else 1
n=abs(n)
y=int(str(n)[::-1])*x

if -2**31 <= y <= 2**31 -1:
      print(y)
else:
      print("0")
