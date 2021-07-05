def is_palindrome(x: int) -> bool:
    return str(x) == str(x)[::-1]


class Solution:
    pass


str_v = is_palindrome(11)
print(str_v)
