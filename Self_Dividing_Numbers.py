a=int(input())
b=int(input())
for i in range(a,b+1):
    count=0
    flag=0
    r=0
    temp=i
    while i:
        r=i%10
        flag+=1
        if r!=0 and temp%r==0:
            count+=1
        else:
            break
        i=i//10
    if count==flag:
        print(temp,end=" ")