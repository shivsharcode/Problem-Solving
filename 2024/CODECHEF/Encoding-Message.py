t = int(input())

while t:
    n = int(input())
    s = input()
    arr = list()
    for i in s:
        arr.append(i)
    
    
    # swap
    i = 0
    while i < n-1:
        arr[i], arr[i+1] = arr[i+1], arr[i]
        i += 2
        
    # encoding
    for i in range(n):
        present_char_ascii = ord(arr[i])  # character to ascii 
        encoded_char_ascii = present_char_ascii - 97
        arr[i] = chr(122-encoded_char_ascii)
        
    ans = ''.join(arr)
    print(ans)
    t-=1 
