# cook your dish here
import math
n = int(input()) #rounds

playerLead = 1 
lead = 0 ;

sum1 = 0 
sum2 = 0

while n :
    p1 , p2 = map(int, input().split())
    
    sum1 += p1 
    sum2 += p2 
    
    currLead = abs(sum1-sum2)
    if currLead > lead :
        lead = currLead
        
        if sum1>sum2 :
            playerLead = 1
        else:
            playerLead = 2      
            
    n-=1 
    
print(f"{playerLead} {lead} ")
