from numpy import ndarray
from scipy.stats import rankdata
from typing import List


def arrayRankTransform(arr: List[int]) -> ndarray:
    return (rankdata(arr, method='dense')).astype(int)


class Solution:
    pass
