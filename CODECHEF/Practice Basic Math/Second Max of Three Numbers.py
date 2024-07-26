n = int(input())
while(n):
    arr = list(map(int, input().split()))
    arr.sort()
    print(arr[1])
    n-=1


