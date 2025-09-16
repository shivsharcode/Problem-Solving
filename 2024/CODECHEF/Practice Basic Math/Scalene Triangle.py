t = int(input())

while t > 0:
    a, b, c = map(int, input().split())
    # Your code goes here
    
    
    sides = {a,b,c} #set
    
    if len(sides) == 3 :
        if( a+b >= c) and ( b+c >=a ) and (a+c >= b) :
            print("YES")
    else:
        print("NO")
        
    t -= 1
