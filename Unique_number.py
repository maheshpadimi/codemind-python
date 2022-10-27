n = int(input())
l = []
flag =0
while n!=0:
    r = n%10
    l.append(r)
    n=n//10
for i in l:
    if l.count(i)>1:
        flag=1
        break
    else:
        flag=0
if flag==1:
    print("Not Unique Number")
else:
    print('Unique Number')