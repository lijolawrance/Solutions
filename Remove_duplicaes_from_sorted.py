from typing import List


def removeDuplicates(nums: List[int]) -> int:
    nums[:] = sorted(list(set(nums)))
    return len(nums)


class Solution:
    pass



