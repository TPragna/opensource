s=input()
x=''
for i in s:
    if 'a'<=i<='z':
        x+=chr(ord(i)-32)
    elif 'A'<=i<='Z':
        x+=chr(ord(i)+32)
print(x)
