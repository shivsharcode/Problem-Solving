# APPROACH - BINARY SEARCH, DP, ARRAY


from bisect import bisect_left   # bisect_left does the work of binary search and returns the position where the number should be inserted
# O(n log(n))
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
         n = len(nums)

         tailTable = []

         for val in nums:
            ind = bisect_left(tailTable, val)    # here bisect_left does the binary search on tailTable and returns the position where val should be inserted in it

            if ind == len(tailTable):
                tailTable.append(val)
            else:
                tailTable[ind] = val
        
         return len(tailTable)

'''
class Solution:
    # O(N^2)
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        dp = [1]*n

        for i in range(1,n):
            for it in range(i):
                if nums[it] < nums[i]:
                    dp[i] = max(dp[i], dp[it]+1 )
        
        return max(dp)
'''
