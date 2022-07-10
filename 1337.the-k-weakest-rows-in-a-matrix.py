#
# @lc app=leetcode id=1337 lang=python3
#
# [1337] The K Weakest Rows in a Matrix
#

# @lc code=start
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return [item[1] for item in sorted([(sum(row), i) for i, row in enumerate(mat)])[:k]]


# @lc code=end
