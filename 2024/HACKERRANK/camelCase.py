def camelcase(s):
    # Write your code here
    count = 1
    for i in s:
        if i == i.upper():
            count += 1
    
    return count
