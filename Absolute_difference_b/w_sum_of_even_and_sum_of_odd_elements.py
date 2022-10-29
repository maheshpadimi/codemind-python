n = int(input())
sum=s=0
lst = list(map(int,input().split()))
for j in lst:
    if j%2==1:
        sum+=j
    else:
        s+=j
print(abs(sum-s))