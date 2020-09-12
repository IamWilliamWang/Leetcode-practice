#
#
# @param s string字符串
# @return bool布尔型
#
class Solution:
    def checkValidString(self, s: str) -> bool:
        stackSize = 0
        magicChar = 0
        for ch in s:
            if ch == '(':
                stackSize += 1
            elif ch == '*':
                magicChar += 1
            elif ch == ')':
                if stackSize:
                    stackSize -= 1
                else:
                    if not magicChar:
                        break
                    magicChar -= 1
        else:
            return stackSize <= magicChar  # 把剩余的（都弹出来
        return False
