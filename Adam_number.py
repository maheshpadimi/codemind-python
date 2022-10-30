n=int(input())
a=n*n
rev=0
riv=0
while n>0:
    rev=rev*10+n%10
    n=n//10
b=rev*rev
while b>0:
    riv=riv*10+b%10
    b=b//10
if a==riv:
    print("True")
else:
    print("False")