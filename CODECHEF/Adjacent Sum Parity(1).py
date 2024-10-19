# this is the first solution, which uses a simple approach of making a boolean array on the basis of ai and ai+1 th element of the b array
# O(n) Time and space complexity
t = int(input())

while t:
    n = int(input()) # size of arr 
    b = list(map(int, input().split()))
    
    a = [None]*n
    
    a[0] = True # let say True for even, False for 'odd'
    
    for i in range(n-1):
        if b[i] == 1:
            a[i+1] = not a[i]
        else:
            a[i+1] = a[i]
        
    # checking validity
    if b[n-1] == 0 and a[0] == a[n-1]:
        print("YES")
    elif b[n-1] == 1 and a[0] != a[n-1]:
        print("YES")
    else:
        print("NO")
        
    t-=1
