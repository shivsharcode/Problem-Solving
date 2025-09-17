class Solution:
    # APPROACH - 01: PYTHONIC APPROACH
    def hammingWeight(self, n: int) -> int:
        
        binarystr = bin(n)[2:]
        ans = binarystr.count('1')
        return ans