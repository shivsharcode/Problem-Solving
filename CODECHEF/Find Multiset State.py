# cook your dish here
# TOTAL COMPLEXITY : O(t) * O(k)
t = int(input())

while t:
    n,k = map(int, input().split())
    arr = list(map(int, input().split())) # sorted array in non-descending (ascending) order
    
    for _ in range(k):
        minVal = arr[0]     # minimum value
        maxVal = arr[-1]    # maximum value
        
        arr.pop()           # pop the maximum value
        arr.pop(0)          # pop the minimum value
        
        arr.append(minVal + maxVal) # appending the sum 
    
    
    print(*arr)
    
    
    t-=1
