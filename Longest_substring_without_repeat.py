class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = {}
        l = r = ans = 0
        n = len(s)
        while (l < n and r < n):
            el = s[r]
            if el in m:
                l = max(l, m[el] + 1)
            m[el] = r
            ans = max(ans, r - l + 1)
            r += 1
        return ans

soln=Solution()
print(soln.lengthOfLongestSubstring('bbbbb'))