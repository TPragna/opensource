X,Y=input().split()
if X==Y:
    print("NULL")
elif((X=='R' and Y=='P') or (X=='P' and Y=='S') or (X=='S' and Y=='R')):
    print("Charan")
else:
    print("Vignesh")
