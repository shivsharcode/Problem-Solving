class Solution:
    # APPROACH - 02 BIT MANIPULATION
    def hammingWeight(self, n: int) -> int:
        ans = 0

        while n != 0:
            lastbit = n & 1
            
            if lastbit == 1:
                ans += 1

            # right shift n
            n = n >> 1

        return ans