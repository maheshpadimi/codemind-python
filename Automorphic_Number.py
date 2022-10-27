n = int(input())
s = n*n
a=b=0
while n!=0 and s!=0:
    a = a*10+n%10
    b = b*10+s%10
    n = n//10
    s = s//10
if a==b:
    print('Automorphic Number')
else:
    print("Not an Automorphic Number")