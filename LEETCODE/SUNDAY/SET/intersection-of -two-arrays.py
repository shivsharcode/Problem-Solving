# BEATS 100% TESTCASES

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)

        ans = set1.intersection(set2)
        ans = list(ans)
        return ans
