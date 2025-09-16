# cook your dish here
t = int(input())

while t:
    n,x,y = map(int, input().split())
    
    pageRead =x*y  
    
    if pageRead < n :
        print("NO")
    else:
        print("YES")
        
    t = t-1
