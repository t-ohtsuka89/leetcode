#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
import collections


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return len(collections.Counter(ransomNote) - collections.Counter(magazine)) == 0


# @lc code=end
