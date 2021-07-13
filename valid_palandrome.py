import re


def isPalindrome(s: str) -> bool:
    regex = '[^A-Za-z0-9]+'
    formatted = re.sub(regex,'', s.lower())
    return formatted[::-1] == formatted


print(isPalindrome("A man, a plan, a canal: Panama"))
