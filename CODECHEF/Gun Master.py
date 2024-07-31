# cook your dish here
t = int(input())

while t:
    n, d = map(int, input().split())
    targetArr = list(map(int, input().split()))
    
    switch = 0 
    closeRange = 0
    longRange = 1 
    
    current = closeRange
    reqd = closeRange
    
    
    for i in targetArr:
        if i > d:
            reqd = longRange
        else:
            reqd = closeRange
            
        if current == reqd :
            pass
        else:
            switch += 1
            current = reqd
            
    print(switch)
        
    t-=1 
