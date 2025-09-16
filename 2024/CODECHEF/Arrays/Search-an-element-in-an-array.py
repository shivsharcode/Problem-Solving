# cook your dish here

arrSize , elem = map(int, input().split())

arr = list(map(int, input().split() ) )

result = "NO"
for i in arr: 
    if i == elem:
        result = "YES"
        break
   

print(result)
