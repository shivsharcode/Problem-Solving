# cook your dish here
n = int(input())

arr = list(map(int, input().split()))

evenCount = 0
oddCount = 0

for i in arr:
    if i%2 == 0 :
        evenCount += 1
    else:
        oddCount += 1

if evenCount > oddCount:
    print("READY FOR BATTLE")
else:
    print("NOT READY")
    
