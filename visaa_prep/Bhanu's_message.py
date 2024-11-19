x=input()
if(x[0]=='+' and x[1:3].isdigit() and x[3]==" " and len(x)==14 and x[4:].isdigit() and sum(int(n) for n in x[4:])>0):
    print("Correct")
else:
    print("Incorrect")
