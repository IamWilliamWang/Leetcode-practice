#
#
# @param s string字符串
# @return bool布尔型
#
class Solution:
    def IsValidExp(self, s):
        # write code here
        def match(ch: str):
            return stack and stack[-1] == '([{'[')]}'.index(ch)]

        stack = []
        for ch in s:
            if ch in '([{':
                stack.append(ch)
            elif ch in ')]}':
                if not match(ch):
                    return False
                stack.pop()
        return True
