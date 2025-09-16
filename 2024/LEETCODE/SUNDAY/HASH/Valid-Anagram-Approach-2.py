# Time complexity : O(n + k)
# Space Complexity : O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sdict = dict()
        tdict = dict()

        for i in range(len(s)):
            if s[i] in sdict:
                sdict[s[i]] += 1
            else:
                sdict[s[i]] = 1
            
            if t[i] in tdict:
                tdict[t[i]] += 1
            else:
                tdict[t[i]] = 1
        
        return sdict == tdict

  '''NOTE: 
  this is slower than Approach 1, because counter is implemented with C implementation, which makes the code runtime faster even though time complexity of this code is somewhat lesser than that one
  '''
