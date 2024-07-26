T = int(input())

while(T):
    
    n = int(input())
    a = list(map(int, input().split() ))
    b = list(map(int, input().split() ))
    
    count = 0
    
    for i in range(n):
        if ( ( a[i] <= 2*b[i] )and ( b[i] <= 2*a[i] ) ):
            count += 1
    
    print(count)
    
    T -= 1 
