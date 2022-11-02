b=int(input())
a=list(map(int,input().split()))
s=0
m,n=map(int,input().split())
for i in a:
    if i<m or i>n:
        s+=i
print(s)