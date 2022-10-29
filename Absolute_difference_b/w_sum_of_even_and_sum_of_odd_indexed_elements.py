n = int(input())
sum=s=0
lst = list(map(int,input().split()))
for j in range(len(lst)):
    if j%2==1:
        sum+=lst[j]
    else:
        s+=lst[j]
print(abs(sum-s))