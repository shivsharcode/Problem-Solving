t = int(input())

def solution(s1, s2):
    min, max = 0, 0
    
    for i in range(len(s1)):
        if s1[i] == '?' or s2[i]== '?':
            max += 1
            
        elif s1[i] != '?' and s2[i] != '?' and s1[i] != s2[i]:
            min += 1
    
    max = max + min
    
    print(min, max)
    return


while t:
    s1 = input()
    s2 = input()
    
    solution(s1, s2)
    
    t-=1
