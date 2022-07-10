#
# @lc app=leetcode id=1337 lang=python3
#
# [1337] The K Weakest Rows in a Matrix
#

# @lc code=start
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        soldiers = list(map(sum, mat))
        l = [(i, s) for i, s in enumerate(soldiers)]
        l.sort(key=lambda item: item[1])
        return [item[0] for item in l[:k]]


# @lc code=end
