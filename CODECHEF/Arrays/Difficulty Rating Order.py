t = int(input())

while(t):
    
    n = int(input())    
    d = list(map(int, input().split()))
    
    result = "Yes"
    
    presentDiff = d[0]
    for i in d:
        if i < presentDiff:
            result = "No"
            break
        presentDiff = i
        
    print(result)
    
    t-=1
