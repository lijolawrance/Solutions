import numpy as np
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        np1 = np.array(nums1)
        np2 = np.array(nums2)
        np3 = np.concatenate((np1, np2))
        return np.median(np3)
'''import statistics
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = statistics.median(nums1+nums2)
        return res'''