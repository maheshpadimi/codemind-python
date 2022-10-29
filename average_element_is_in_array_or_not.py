def fun(n,arr,avg):
    if avg in arr:
        print("True")
    else:
        print("False")
n = int(input())
arr = list(map(int,input().split()))
avg = sum(arr)//n
fun(n,arr,avg)