# PYTHON SUBMISSION USING HASHMAPS
t = int(input())

while(t>0):
    n = int(input()) # BINARY STRING LENGTH
    s = input() #BINARY STRING
    
    # CODE
    m = {
        "00" : 'A',
        "01" : 'T',
        "10" : 'C',
        "11" : 'G'
    }
    
    result = ""
    
    for i in range(0, len(s), 2):
        substr = s[i: i+2]
        result = result + m[substr] 

  
    print(result)
    t -= 1
