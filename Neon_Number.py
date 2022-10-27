n = int(input())
s = n*n
flag=0
for i in range(s):
    r = s%10
    flag+=r
    n=n//10
if flag==s:
    print("Neon Number")
else:
    print("Not Neon Number")