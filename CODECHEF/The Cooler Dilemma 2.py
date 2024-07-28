t = int(input())
while t :
    
    x, y = map(int, input().split())
    
    monthCount = y // x ;
    
    if y%x == 0 :
        print(monthCount-1)
    else:
        print(monthCount)
    
    t-=1 
