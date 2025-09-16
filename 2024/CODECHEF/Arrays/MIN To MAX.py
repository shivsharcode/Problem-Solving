t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    # Your code goes here
    
    minVal = min(a) # finds the minimum value in the list
    count = 0 
    
    for i in a:
        if i != minVal:
            count += 1
            
    print(count)
    
    t -= 1
