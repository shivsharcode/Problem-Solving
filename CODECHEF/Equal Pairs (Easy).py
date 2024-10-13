import math

def combinations(num):
    # with r = 2
    num = (num * (num-1))//2
    return num

def max_pairs(arr, n):
    
    freq = {} # dictionary of the elements frequency
    zeroCount = 0
    
    for i in arr:
        if i == 0:
            zeroCount += 1
        else:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
    
    totalPairs = 0
    maxFreq = 0
    
    for i in freq.values():
        totalPairs += combinations(i) # combination pairs of each non zero element
        if i > maxFreq:
            maxFreq = i
        
    if zeroCount > 0:
        # if there are any zero elements replace the zero with the elemnet with highest frequency
        totalPairs += combinations(maxFreq + zeroCount) - combinations(maxFreq)
    
    
    return totalPairs
    
    
    

# MAIN

t = int(input())  # input test cases
while t:
    
    n = int(input())
    arr = list(map(int, input().split()))
    
    maximumPairs = max_pairs(arr, n)
    print(maximumPairs)
    
    t-=1
