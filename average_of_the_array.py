def fun(n,arr,avg):
    print("{:.2f}".format(avg))
n = int(input())
arr = list(map(int,input().split()))
avg = sum(arr)/n
fun(n,arr,avg)