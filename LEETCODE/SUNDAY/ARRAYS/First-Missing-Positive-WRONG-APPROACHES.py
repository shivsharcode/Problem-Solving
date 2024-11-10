'''first
APPROACH : USE OF 'in' opearator 
Time Complexity : O(n^2)
Space Complexity : O(1)

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        smallest = 1
        
        for _ in nums:
            if smallest in nums:
                smallest += 1
            else:
                return smallest
        
        return smallest
'''

'''
second
APPROACH : Visited Array
Time Comp : O(n)
Space : O(n)

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        vis = [False]*(n+1)

        #visited array
        for val in nums:
            if 0 < val <= n:
                vis[val] = True
        
        for i in range(1, n+1):
            if not vis[i]:
                return i


        return n+1
'''

'''
