import numpy as np
from typing import List

from numpy import ndarray


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> ndarray:
    np1 = np.array(nums1)
    np2 = np.array(nums2)
    np3 = np.concatenate((np1, np2))
    return np.median(np3)


class Solution:
    pass
'''import statistics
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = statistics.median(nums1+nums2)
        return res'''