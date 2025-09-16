# cook your dish here
t = int(input())

while t:
    
    x,y = map(int, input().split() )
    
    smaller = min(x,y)
    bigger = max(x,y)
    
    operation = 0
    
    
    while 2*smaller > bigger:
        smaller -=1
        operation+=1
    else:
        print(operation)
        
    t-=1
