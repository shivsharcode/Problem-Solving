def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong  
    special_characters = "!@#$%^&*()-+"
    
    countNum = 0
    countLower = 0
    countUpper = 0
    countSpecial = 0
    
    # keeping count of each character in the current Passwrod string
    for i in password:
        if i.isdigit():
            countNum = 1
        elif i.islower():
            countLower = 1
        elif i.isupper():
            countUpper = 1
        elif i in special_characters:
            countSpecial = 1
            
    # calculating the characters Needed for STRONG Password
    
    charPresent = countNum + countLower + countUpper + countSpecial
    charNeeded = 4- charPresent
    
    
    # determing the length condition of password
    currentLength = len(password) + charNeeded
    
    if currentLength < 6:
        charNeeded += (6-currentLength)
     
    # returning the character needed
    return charNeeded
    
    
    
