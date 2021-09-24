from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        indices = [i for i, x in enumerate(nums) if x == target]
        if len(indices) == 0:
            return [-1, -1]
        else:
            return [indices[0], indices[len(indices) - 1]]


soln = Solution()
print(soln.searchRange(nums=[1, 7, 1, 7, 7, 8], target=7))
