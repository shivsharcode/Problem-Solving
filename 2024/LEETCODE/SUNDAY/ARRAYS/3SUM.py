class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)
        ans = []

        for i in range(len(nums)-2):

            # removing duplicacy, the sorted array will help us
            if i>0 and nums[i] == nums[i-1]:
                continue

            j = i+1
            k = len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    j+=1
                    # skipping duplicates of j
                    while j<k and nums[j] == nums[j-1] :
                        j += 1 
                elif total < 0:
                    j += 1
                elif total > 0:
                    k -= 1

        return ans
                    
