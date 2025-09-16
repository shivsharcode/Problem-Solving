
class Solution:
    def isHappy(self, n: int) -> bool:

        num = n
        uniqueSq = set()
        while num > 3 and num not in uniqueSq:
            s = str(num)
            uniqueSq.add(num)
            num = 0
            for i in s:
                num += int(i)**2
            
        return num == 1


'''
class Solution:
    def isHappy(self, n: int) -> bool:

        num = n
        uniqueSq = set()
        while num != 1 and num not in uniqueSq:  # SLIGHT CHANGE
            uniqueSq.add(num)
            s = str(num)
            num = 0
            for i in s:
                num += int(i)**2
            
        return num == 1
'''

# SINCE THIS APPROACH USES LIST COMPREHENSION, IT IS THE SLOWEST
'''
class Solution:
    def isHappy(self, n: int) -> bool:

        num = n
        uniqueSq = set()
        while num != 1 and num not in uniqueSq:
            uniqueSq.add(num)
            num = sum(int(i)**2 for i in str(num)) # sum of squares in a single line 

        return num == 1
'''

