a = int(input())
b=a
s=0
while a!=0:
    r = a%10
    p=1
    for i in range(1,r+1):
        p*=i
    s+=p
    a=a//10
if s==b:
    print("The number",b,"is a strong number")
else:
    print("The number",b,"is not a strong number")