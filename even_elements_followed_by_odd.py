n=int(input())
a=list(map(int,input().split()))
l=[]
for i in a:
    if i%2==0:
        l.append(i)
for j in a:
    if j%2==1:
        l.append(j)
for i in l:
    print(i,end=" ")