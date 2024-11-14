N=int(input())
if N<1 or N>12:
    print("Invalid")
elif 3<=N<=5:
    print("Spring")
elif 6<=N<=8:
    print("Summer")
elif 9<=N<=11:
    print("Autumn")
else:
    print("Winter")
