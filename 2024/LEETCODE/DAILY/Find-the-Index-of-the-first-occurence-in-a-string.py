# APPROACH - SLIDING WINDOW
# O(n-k)*O(2*k) = O(n.k)

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
        
        left = 0
        right = len(needle) -1

        while right < len(haystack): # O(n-k)
            if haystack[left:right+1] == needle: # O(2k)
                return left

            right += 1
            left+= 1
                
        return -1
        
