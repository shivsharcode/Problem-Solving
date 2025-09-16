# cook your dish here
# Time Complexity - O(N/2)

import math

def primeNumber(n):
    
    if n<=1 : 
        return "no" ;
    if n == 2:
        return "yes" ;
    if n%2 == 0 :
        return "no" ;
    
    for i in range(3, int(math.sqrt(n))+1, 2):
        if n%i == 0:
            return "no" 
    
    return "yes"
    



t = int(input())
while t :
    n = int(input())
    result = primeNumber(n)
    print(result)
    
    t-=1
