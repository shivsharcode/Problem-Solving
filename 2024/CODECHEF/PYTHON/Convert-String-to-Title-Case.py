
T = int(input())  #TESTCASES

while(T):
    
    s = input() #INPUT STRING
    
    parts = s.split(" ") #SPLIT THE STRING WHEN SPACE APPEAR , FORMS A LIST OF THE WORDS 
    
    result = ""
    
    for i in parts:
        if not( i.upper() == i  ):  #LEAVE THE ACRONYM
            i = i.capitalize()
            
        result = result + " " + i 
    

    print(result)
    T -= 1 
