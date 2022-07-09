#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        ans: int = 0
        for i, c in enumerate(s):
            c_value = dic[c]
            if i < len(s) - 1:
                next_c_value = dic[s[i + 1]]
                if c_value < next_c_value:
                    c_value *= -1
                    ans += c_value
                elif c_value > next_c_value:
                    ans += c_value
                else:
                    ans += c_value
            else:
                ans += c_value
        return ans


# @lc code=end
