a = int(input())
b = int(input())
count=0
flag=0
for i in range(1,a):
    if a%i==0:
        count+=i
for j in range(1,b):
    if b%j==0:
        flag+=j
if count==b and flag==a:
    print('Amicable')
else:
    print('Not Amicable')