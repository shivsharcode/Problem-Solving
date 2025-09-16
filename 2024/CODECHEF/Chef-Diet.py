# O(n) - Time Complexity
def diet(arr, n, k):
    carry = 0
    for i in range(n):
        if arr[i] + carry >= k:
            carry = arr[i]+carry - k
        else:
            print(f"NO {i+1}")
            return 
    
    print("YES")
    

t = int(input())

while t:
    n,k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    diet(arr, n, k)
    t-=1
