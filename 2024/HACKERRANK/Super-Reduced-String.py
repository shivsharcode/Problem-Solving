def superReducedString(s):
    # Write your code here
    stack = []
    
    for char in s:
        if (stack) and (stack[-1] == char):     # if stack is not empty and last elem == char
            stack.pop()     # delete the last character of stack
        else:
            stack.append(char)
            
    result = ''.join(stack)     # result string 
    
    if len(result):
        return result
    else:
        return "Empty String"
   
   
   
