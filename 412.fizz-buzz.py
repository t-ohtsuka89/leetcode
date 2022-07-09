#
# @lc app=leetcode id=412 lang=python3
#
# [412] Fizz Buzz
#

# @lc code=start
class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        ans = []
        for i in range(1, n + 1):
            is_fizz = i % 3 == 0
            is_buzz = i % 5 == 0
            if is_fizz and is_buzz:
                ans.append("FizzBuzz")
            elif is_fizz:
                ans.append("Fizz")
            elif is_buzz:
                ans.append("Buzz")
            else:
                ans.append(str(i))
        return ans


# @lc code=end
