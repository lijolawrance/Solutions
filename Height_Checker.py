import numpy as np
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ab = np.array(heights)
        ab.sort()
        return sum(heights != ab)