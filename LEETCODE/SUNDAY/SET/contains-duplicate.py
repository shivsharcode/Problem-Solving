# EASY

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        myset = set(nums)

        return not( len(myset) == len(nums) )
            
