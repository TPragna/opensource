x,y,z=map(int,input().split())
if x>z:
    print('0')
else:
    if x+y>z:
        print('1')
    else:
        print('2')
