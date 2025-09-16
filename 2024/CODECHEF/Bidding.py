# cook your dish here
t = int(input())

while t:
    a, b, c = map(int, input().split())
    
    if a > b : 
        if a > c :
            print("Alice")
        else:
            print("Charlie")
    elif b > a :
        if b > c :
            print("Bob")
        else:
            print("Charlie")
        
    
    t-=1 
