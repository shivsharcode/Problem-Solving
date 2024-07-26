# cook your dish here
T = int(input())

while(T):
    a, b = map(int, input().split())
    
    print(a%b)
    T-=1 
