from scipy.stats import rankdata
class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        return (rankdata(arr, method='dense')).astype(int)