# cook your dish here
T = int(input())

while(T):
    
    arrSize = int(input()) ;
    
    max = 0 
    
    for i in range(arrSize):
        val = int(input()) 
        if max < val:
            max = val
    
    
    print(max)
    
    T-=1
