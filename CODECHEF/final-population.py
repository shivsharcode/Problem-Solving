# cook your dish here
t = int(input())

while t:
    x, y, z = map(int, input().split())
    
    print(x-y+z)
    t-=1 
