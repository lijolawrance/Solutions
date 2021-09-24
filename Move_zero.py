from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        print(len(nums))
        ct = nums.count(0)
        nums[:]=filter(lambda x: x != 0, nums)
        #nums[:] = (value for value in nums if value != 0)
        nums.extend([0] * ct)
        #nums.extend(0 for i in range(ct))

        print(ct)
        print(nums)


soln = Solution()

soln.moveZeroes([0, 1, 0, 3, 12])
