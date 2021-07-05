from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        sub= target - nums[i]
        if sub in nums[i+1:]:
            return i, nums.index(sub,i+1)


class Solution:
    pass