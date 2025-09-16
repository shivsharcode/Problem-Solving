# cook your dish here
import math
t = int(input())

while t :
    grpSize, subCost = map(int, input().split())
    
    n = math.ceil(grpSize/6)
    print(n* subCost)
    t-=1 
    
