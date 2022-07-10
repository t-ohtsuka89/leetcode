#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start


class Solution:
    def twoSum(self, nums, target):
        dic = {}
        for i, num in enumerate(nums):
            if num in dic:
                return [dic[num], i]
            else:
                dic[target - num] = i


# @lc code=end
