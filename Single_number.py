from functools import reduce
from typing import List


def singleNumber(nums: List[int]) -> int:
    return reduce(lambda x, y: x ^ y, nums)
    # return (2 * sum(set(nums)) - sum(nums)) // 1


print(singleNumber([1, 2, 3, 1, 2, 1]))
