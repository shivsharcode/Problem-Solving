# cook your dish here
t = int(input())

while t:
    n, k = map(int, input().split())
    
    if n < k :
        print("YES")
    else:
        print("NO")
    
    t-=1 
