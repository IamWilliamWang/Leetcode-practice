#
# 翻译组合数
# @param num int整型 数字加密报文
# @return int整型
#
class Solution:
    def translateNum(self, num):
        def dp(i: int):
            nonlocal result
            if i == len(s):
                result += 1
                return
            dp(i + 1)
            if i < len(s) - 1 and int(s[i] + s[i + 1]) < 26:
                dp(i + 2)

        s = str(num)
        result = 0
        dp(0)
        return result
