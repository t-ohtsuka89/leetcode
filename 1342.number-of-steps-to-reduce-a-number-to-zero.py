#
# @lc app=leetcode id=1342 lang=python3
#
# [1342] Number of Steps to Reduce a Number to Zero
#

# @lc code=start
class Solution:
    def numberOfSteps(self, num: int) -> int:
        bin_num = bin(num)[2:]
        n_one = bin_num.count("1")
        return n_one + len(bin_num) - 1


# @lc code=end
