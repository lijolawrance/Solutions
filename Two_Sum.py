class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            sub= target - nums[i]
            if sub in nums[i+1:]:
                return i, nums.index(sub,i+1)