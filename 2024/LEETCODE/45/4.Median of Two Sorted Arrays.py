class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        nums1.extend(nums2)  #merging the two arrays
        nums1.sort()        # sorting the arrays - merge sort by default 

        n = len(nums1)

        if n % 2 == 0:  #even
            return  (nums1[n//2 -1] + nums1[ (n//2)+1 -1] )/2      # -1 in the formulas bcoz of the 0 base indexing
        else:
            return  nums1[(n+1)//2 -1] 
