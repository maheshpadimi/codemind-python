n = int(input())
for i in range(n):
    n = int(input())
    fact=1
    i=1
    while i<=n:
        fact=fact*i
        i+=1
    print(fact)