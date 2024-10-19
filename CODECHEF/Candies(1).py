# cook your dish here


def solution(arr):
    
    myDict = dict()
    
    for i in range(len(arr)):
        if arr[i] in myDict:
            myDict[arr[i]] += 1
        else:
            myDict[arr[i]] = 1
        
    for i in myDict:
        if myDict[i] > 2:
            return "NO"
    
    
    return "YES"
    


t = int(input())

while t:
    n = int(input()) # number of cities
    
    arr = list(map(int, input().split()))
    
    ans = solution(arr)
    print(ans)
    
    t-=1 
