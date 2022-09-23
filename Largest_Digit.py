n = int(input())
l=[]
while n>0:
    r = n%10
    l.append(r)
    n=n//10
l = sorted(l)
print(l[-1])