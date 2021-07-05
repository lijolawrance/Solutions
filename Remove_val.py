from typing import List


def removeElement(nums: List[int], val: int) -> int:
    for i in range(nums.count(val)):
        nums.remove(i)
    return len(nums)


class Solution:
    pass
