from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        n = len(p)
        left, right = 0, n-1

        p_dict = Counter(p)                 
        mydict = Counter(s[left:right+1])

        if mydict == p_dict:
            ans.append(left)

        # sliding the window
        for right in range(n, len(s)):
            # handling the left char
            if mydict[s[left]] > 1:
                mydict[s[left]] -= 1
            else:
                del mydict[s[left]]
            
            left += 1   # moving left forward

            # handling the new right char
            if s[right] in mydict:
                mydict[s[right]] += 1
            else:
                mydict[s[right]] = 1

            # sliding window updated, now comparing the dicts, checking sliding windown and p anagram
            if mydict == p_dict:
                ans.append(left)

        return ans
