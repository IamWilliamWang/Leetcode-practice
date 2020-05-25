import re


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return re.findall('^' + p + '$', s) != []


print(Solution().isMatch("aa", "a"))
