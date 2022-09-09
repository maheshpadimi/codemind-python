n=int(input())
a=0
for i in range(n):
    for j in range(n):
        if (i**2) + (j**2) == n:
            a+=1
if a==0:
    print("False")
else:
    print("True")