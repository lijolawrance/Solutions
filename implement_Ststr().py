def strStr( haystack: str, needle: str) -> int:
    return haystack.index(needle) if needle in haystack else -1


print(strStr("hello", "ll"))

print(strStr("aaaaa","bba"))
print(strStr("",""))