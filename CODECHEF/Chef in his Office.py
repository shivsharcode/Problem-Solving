# cook your dish here
t = int(input())

while t:
    x, y = map(int, input().split())
    
    print(x*4 + y)
    t-=1 
