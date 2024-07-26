t = int(input())

while t>0 :
    
    n = int(input())
    temp = n
    digSum = 0
    while temp != 0:
        digit = temp % 10 
        digSum = digSum + digit
        temp = temp // 10
    
    print(digSum)
    
    
    t-=1 
