n = int(input())
for i in range(n):
    l,r  = map(int,input().split())
    s = 0
    for j in range(l,r+1):
        if j%10==2 or j%10==3 or j%10==9:
            s+=1
    print(s)