class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        subarr_count = 0
        prefix_sum = 0
        prefix_sum_dict = dict()    
        prefix_sum_dict = {0:1}

        for ind, num in enumerate(nums):

            prefix_sum += num
            
            # checking if there is any subarray in between
            if prefix_sum - k in prefix_sum_dict :
                subarr_count += prefix_sum_dict[prefix_sum - k]
                       
            # storing the current prefix_sum if not previously present
            if prefix_sum not in prefix_sum_dict:
                prefix_sum_dict[prefix_sum] = 1
            else:
                # if the prefix_sum is there in the dictionary
                prefix_sum_dict[prefix_sum] += 1
            
        return subarr_count
