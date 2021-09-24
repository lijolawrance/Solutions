from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[int]:
        dp = [[] for _ in range(target + 1)]
        print(dp)
        for c in candidates:  # O(N): for each candidate
            for i in range(c, target + 1):  # O(M): for each possible value <= target
                if i == c: dp[i].append([c])
                print(dp)
                for comb in dp[i - c]: dp[i].append(comb + [c])  # O(M) worst: for each combination
        return dp[-1]


S = Solution()
print(S.combinationSum([2,3,6,7], 7))
