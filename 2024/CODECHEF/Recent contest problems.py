# cook your dish here
t = int(input())

while t:
    
    
    n = int(input()) # total probllems in the recent 2 contest
    contests = list(input().split() )
    
    contest1 = 0 
    contest2 = 0 
    
    for i in contests:
        if i == "START38":
            contest1 += 1
        else:
            contest2 += 1 
            
    
    print(f"{contest1} {contest2}")
    
    
    t-=1 
