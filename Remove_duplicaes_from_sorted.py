class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        nums[:] = sorted(list(set(nums)))
        return len(nums)
