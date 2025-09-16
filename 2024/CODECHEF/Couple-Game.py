# cook your dish here
t = int(input())

while t:
    g,b = map(int, input().split())
    
    # the number girls participated is full strength bcoz b > g 
    # therefore the b-g boys couldn't participate 
    
    print(b-g)
    
    
    t-=1 
