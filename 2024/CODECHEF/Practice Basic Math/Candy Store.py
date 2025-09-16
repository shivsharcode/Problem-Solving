t = int(input())

while t > 0:
    x, y = map(int, input().split())
    # Your code goes here
    
    if(y > x):
        print(x + (y-x)*2)
    else:
        print(y)
    
    t -= 1
