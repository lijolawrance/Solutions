from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_value = nums[0]
        cur_value = 0
        for n in nums:
            if cur_value < 0: cur_value = 0
            cur_value += n
            max_value = max(max_value, cur_value)
        return max_value


s = Solution()
print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(s.maxSubArray([5, 4, -1, 7, 8]))
