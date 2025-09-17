class Solution:
    # APPROACH - 03 : BRIAN KERNIGHAN'S ALGO (BIT MANIPULATION)
    # TIME COMPLEXITY : O(no. of set bits)  == O(no of '1' bits)

    """
    Key Idea:
        * Subtracting 1 from a number flips all bits after the rightmost set bit('1') including the bit itself
        * Doing ` n & (n-1) ` removes the the rightmost set bit
        * So if we repeat this until n becomes 0, the number of times the loop runs = number of set bits '1'
    """

    def hammingWeight(self, n: int) -> int:
        ans = 0

        while n != 0:
            n = n & (n - 1)  # removed rightmost set bit ('1')
            ans += 1

        return ans