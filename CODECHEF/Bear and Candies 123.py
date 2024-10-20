# cook your dish here
t = int(input())

while t:
    a,b  = map(int, input().split())
    
    limak = 1
    bob = 2
    while True:
        if limak <= a:
            a -= limak
            limak += 2
        else:
            print("Bob")
            break
        
        if bob <= b:
            b-= bob
            bob += 2
        else:
            print("Limak")
            break
            
    t-=1 
