import numpy as np
class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        return np.cumsum(np.array(nums))