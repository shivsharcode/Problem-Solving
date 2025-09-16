# cook your dish here
# Time Complexity - O(N)
# Approach - bruteForce

def primeNumber(n):
    count = 0 
    
    for i in range(1,n+1) :
        if n%i == 0 :
            count+= 1 
            
    if count == 2:
        return "yes"
    else:
        return "no"
        


t = int(input())
while t :
    n = int(input())
    result = primeNumber(n)
    print(result)
    
    t-=1
