class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        count = 0
        for j in range(len(typed)):
            if count < len(name) and name[count] == typed[j]:
                    count += 1
            elif count == 0 or name[count-1] != typed[j]:
                    return False
        return count == len(name)