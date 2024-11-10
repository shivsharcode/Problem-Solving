# APPROACH : BRUTE FORCE
# TIME : O(N^2)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        ans = []
        i = 0

        while i< len(nums) -1:
            j = i+1
            while j<len(nums):
                if nums[i] + nums[j] == target:
                    ans = [i,j]
                    return ans
                else:
                    j+= 1
            i+=1     
        
        return ans


