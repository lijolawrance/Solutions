class Solution:
    def is_palindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
        '''lst = list(str(x))
        if lst == lst[::-1]:
            return True
        else:
            return False'''


strv = Solution().is_palindrome(11)
print(strv)
