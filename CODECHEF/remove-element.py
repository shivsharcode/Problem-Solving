class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k+= 1

        return k  


'''
class Solution:
# This approach can have a worst case of O(n^2) when there are many val recurrent values

    def removeElement(self, nums: List[int], val: int) -> int:
        valCount = nums.count(val)
        k = len(nums) - valCount
        i = 0
        
        for i in range(k):
            if nums[i] == val:
                j = i+1
                while nums[i] == nums[j]:
                    j += 1
                # swap
                nums[i], nums[j] = nums[j], nums[i]
                
        return k
'''


