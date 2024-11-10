class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #CYCLE SORT

        n = len(nums)
        i = 0

        while i < n:
            val = nums[i]
            correctIndex = val - 1

            # check
            if (val > 0 and val <= n) and nums[i] != nums[correctIndex]:
                #swap
                nums[i], nums[correctIndex] = nums[correctIndex], nums[i]
            else:
                i += 1

        # now for each element in its correct order the value == index + 1
        # the first occurance of index where the condition doesn't specify gives the smallest positive number not present
        for i in range(n):
            if nums[i] != i + 1:
                return i+1

        # if all are at their respective correct position
        return n+1
    
