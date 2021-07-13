def lengthOfLastWord(s: str) -> int:
    if s.isspace():
        return 0
    lst = s.strip().split(" ")
    return len(lst[-1])


print(lengthOfLastWord('H '))
