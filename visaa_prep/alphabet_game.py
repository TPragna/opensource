s=input()
vol,con=0,0
for i in s:
    if i.lower() in 'aeiou':
        vol+=1
    elif 'a'<=i.lower()<='z':
        con+=1
print(f"{vol},{con}")
