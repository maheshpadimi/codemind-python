from math import sqrt
n = int(input())
a = int(sqrt(n))
b = a*(a+1)
if b==n:
    print("YES")
else:
    print("NO")