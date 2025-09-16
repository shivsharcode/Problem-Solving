class Solution:

    def longestSubstrDistinctChars(self, s):
        # code here
        char_set = set()
        left = 0
        maxLen = 0
        
        for right in range(len(s)):
            
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            char_set.add(s[right])
            maxLen = max(maxLen, len(char_set))
            
        return maxLen
