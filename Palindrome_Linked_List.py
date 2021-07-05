# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_val=None):
        self.val = val
        self.next = next_val


def isPalindrome(self, head: ListNode) -> bool:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result == result[::-1]
