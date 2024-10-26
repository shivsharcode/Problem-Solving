# cook your dish here

def solution(arr, n):
    
    normal = 0
    
    for i in range(n):
        
        end = i+1
        while end <= n:
            subarr = arr[i: end]
            
            
            subArr = sorted(subarr)
            median = subArr[len(subArr)//2]
            mean = sum(subArr)/len(subArr) 
            
            if mean == median:
                print(subarr, f"mean = {mean}, median = {median}")
                normal += 1
            # print(subArr, f"beg = {i}, end={end}")
            
            end += 1
        
    return normal
    
    
t = int(input())

while t:
    n = int(input())
    arr = list(map(int, input().split()))
    
    ans = solution(arr, n)
    print(ans)
    t-=1
