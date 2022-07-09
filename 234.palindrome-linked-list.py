#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
import math
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: ListNode | None = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        path = []
        while True:
            path.append(head.val)
            if head.next is None:
                break
            else:
                head = head.next
        n_half = math.ceil(len(path) / 2)
        for i in range(n_half):
            forward = path[i]
            backward = path[-(i + 1)]
            if forward != backward:
                return False
        return True


# @lc code=end
