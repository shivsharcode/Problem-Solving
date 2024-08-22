t = int(input())

while t :
     x, y = map(int, input().split())
     
     if x < y :
         print(y-x)
     else:
         print(0)
     
     t-=1
