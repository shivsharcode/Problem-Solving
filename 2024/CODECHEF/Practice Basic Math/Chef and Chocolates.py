t = int(input())

while t > 0:
    x, y, z = map(int, input().split())
    # Your code goes here
    totalMoney = x*5 + 10*y
    print(totalMoney//z)
    t -= 1
