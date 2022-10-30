n=int(input())
a=list(map(int,str(n)))
if len(a)==10 and a[0]!=0:
    print("Valid")
else:
    print("Invalid")