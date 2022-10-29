n = int(input())
sum=0
lst = list(map(int,input().split()))
for j in range(len(lst)):
    if j%2==1:
        sum+=lst[j]
print(sum)