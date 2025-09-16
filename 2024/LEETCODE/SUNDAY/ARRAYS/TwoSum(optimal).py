# In this approach we've made a dictionry, we'll iterate the nums array once and for each element we'll check wheter target-element exists in the dictionary, 
# if it does then we've got the pair :), but if not then we'll append the element with its position in the dictionary

# O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {} 
        n = len(nums)

        for i in range(n):
            diff = target - nums[i] 
            # checking if the difference exists in the dict
            if diff in myDict:
                return [i, myDict[diff]]
            else: # update the dictionary by adding this number
                myDict[nums[i]] = i
