#
#
# @param str string字符串
# @return string字符串
#
class Solution:
    def compress(self, rawStr: str) -> str:
        ans = ''
        char = ''
        counter = 0
        for ch in rawStr:
            if ch != char:
                if char:
                    ans += char + str(counter)
                char = ch
                counter = 1
            else:
                counter += 1
        ans += char + str(counter)
        return ans if len(ans) <= len(rawStr) else rawStr
