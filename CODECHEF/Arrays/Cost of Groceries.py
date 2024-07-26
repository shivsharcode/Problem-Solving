t = int(input())

while(t):
    
    n, x = map(int, input().split() )
    a = list(map(int, input().split() ))
    b = list(map(int, input().split() ))
    
    totalCost = 0
    
    for i in range(n):
        if a[i] >= x :
            totalCost += b[i]
        
    print(totalCost)
    
    t-=1
