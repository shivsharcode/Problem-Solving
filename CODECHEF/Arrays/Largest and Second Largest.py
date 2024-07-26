t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    
    largest = max(a)
    secondLargest = 0
    
    for i in a:
        if (secondLargest < i) and (i < largest):
            secondLargest = i
        
    print(largest + secondLargest)
    t -= 1
