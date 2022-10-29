n = int(input())
sum=0
lst = list(map(int,input().split()))
for j in lst:
    if j%2==0:
        sum+=j
print(sum)