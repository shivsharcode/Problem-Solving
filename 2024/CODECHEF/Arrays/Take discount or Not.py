t = int(input())

while(t):
    n,x,y = map(int, input().split())
    priceArr = list(map(int, input().split()))
    
    initialSum = sum(priceArr)
    
    for i in range(n):
        if priceArr[i]<y:
            priceArr[i] = 0
        else:
            priceArr[i] = priceArr[i]-y
        
    newSum = sum(priceArr) + x 
    
    # print(f"{initialSum}, {newSum}")
    if newSum < initialSum:
        print("COUPON")
    else:
        print("NO COUPON")
    
    t-=1
