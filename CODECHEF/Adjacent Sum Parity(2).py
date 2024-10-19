# complexity O(1) - space/time

t = int(input())

while t:
    n = int(input())
    arr = list(map(int, input().split()))
    
    number_of_ones = arr.count(1)
    
    # for even parity the sum of all the ones in the arr should be a even number otherwise it would not be even parity (i.e odd parity)
    
    if number_of_ones % 2 == 0:
        print("YES")
    else:
        print("NO")
    t-=1 
