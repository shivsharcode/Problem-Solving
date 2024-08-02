# cook your dish here
t = int(input())

while t:
    x,y,z = map(int, input().split())
    
    totalStudents = x * y
    
    if z > (totalStudents/2):
        print("Yes")
    else:
        print("No")
    
    t-=1 
