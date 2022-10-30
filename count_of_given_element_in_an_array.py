n=int(input())
count=0
arr=list(map(int,input().split()))
z = int(input())
for i in arr:
    if i==z:
        count+=1
print(count)