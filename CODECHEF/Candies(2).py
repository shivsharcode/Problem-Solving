# Time : O(n2)
# space : O(1)


t = int(input())

while t:
    n = int(input()) # number of cities

    arr = list(map(int, input().split()))
    
    for i in arr:
        if arr.count(i) > 2:
            print("NO")
            break
    else:
        print("YES")
    t-=1 
