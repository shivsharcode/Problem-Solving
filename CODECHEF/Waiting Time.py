# cook your dish here
t = int(input())

while t:
    k, x = map(int, input().split())
    totalDays = 7 * k 
    
    print(totalDays-x)
    t-=1 
