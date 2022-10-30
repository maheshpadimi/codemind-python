n = int(input())
a,b = 0,1
i = 0
while i<n:
    print(a,end=" ")
    c = a + b
    a = b
    b = c
    i += 1