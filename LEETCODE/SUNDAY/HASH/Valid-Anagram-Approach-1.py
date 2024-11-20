# Time Complexity : O(n+k), O(n) for dictionaries and O(k) for comparision
# Space Complexity : O(k)

from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sdict = Counter(s)
        tdict = Counter(t)
        
        return sdict == tdict

'''NOTE:
This code is faster in runtime than Approach-2, this is because of the C-implementation of Counter function
'''
