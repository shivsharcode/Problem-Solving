# cook your dish here
t = int(input())

while t:
    n, x = map(int, input().split())
    
    
    # odd + odd = even 
    # even + even = even 
    
    # odd + even = odd 
    
    if n % 2 == 0:
        print("YES")
    else:
        if x%2 != 0:
            print("YES")
        else:
            print("NO")
            
    t-=1
