class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, k = len(haystack), len(needle)
        if n < k :
            return -1
        
        # RABIN KARP
        base = 256 # the len of all chars
        prime = 101

        texthash = 0
        patternhash = 0
        h = 1

        # initialising h
        for _ in range(k-1):
            h = (h * base) % prime
        
        # initialising the starting texthash & patternhash
        for i in range(k):
            texthash = ( texthash * base + ord(haystack[i]) ) % prime
            patternhash = (patternhash * base + ord(needle[i]) ) % prime

        # sliding windown -- rolling hash
        left = 0
        right = k-1

        while right < n :
            if patternhash == texthash:
                if haystack[left: right+1] == needle:
                    return left
            
            if right < n-1:
                texthash = (texthash - (h * ord(haystack[left]) )%prime )% prime
                texthash = (texthash*base + ord(haystack[right+1])) % prime
            
            left += 1
            right += 1

        return -1

