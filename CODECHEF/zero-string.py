# cook your dish here
def solution(s):
    onesCount = s.count('1')
    zeroCount = s.count('0')
    
    if zeroCount >= onesCount:
        # only need to delete the ones
        print(onesCount)
        return
    else:
        print(zeroCount + 1)
        return 
    
    
t = int(input())

while t:
    n = int(input())
    s = input()
    
    solution(s)
    t-=1
