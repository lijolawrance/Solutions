from functools import reduce
from typing import List


def singleNumber(nums: List[int]) -> int:
    print(3 * sum(set(nums)))
    print(sum(nums))
    return (3 * sum(set(nums)) - sum(nums)) // 2


print(singleNumber([2, 2, 21, 2]))
