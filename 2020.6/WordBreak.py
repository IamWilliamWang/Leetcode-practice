from typing import List
from collections import Counter
from itertools import chain

from test_script import speedtest


class Solution:
    def wordBreak_slow(self, s: str, wordDict: List[str]) -> bool:
        wordCounter = Counter(chain(*[[ch for ch in string] for string in wordDict]))  # 统计wordDict里的所有字符
        sCounter = Counter(s)  # 统计s中所有的字符
        for sChar in sCounter:  # 如果s里出现了wordDict没有的字符，就是False
            if sChar not in wordCounter:
                return False
        stack = []  # 保存i, j指针
        i, j = 0, -1
        wordDictCharsSet = set(wordDict)  # 把List变成Set，提升速度
        iBlacklist = set()  # i的黑名单
        while True:
            j += 1
            if j >= len(s):  # 如果j越界
                if i >= len(s):  # 检查i如果也越界就说明True
                    return True
                else:
                    iBlacklist.add(i)  # 否则加入i到黑名单中
                    if len(s) > 150:  # 解决超时的偷懒补丁
                        while stack:  # 如果得到的i在黑名单则跳过
                            i, j = stack.pop()
                            j += 1
                            if i not in iBlacklist:
                                break
                    if not stack:  # 如果栈为空，则False
                        break
                    if len(s) <= 150:  # 如果不会超时则，弹出i和j再挨个试
                        i, j = stack.pop()
                        j += 1
            if s[i:j + 1] in wordDictCharsSet:  # 得到i, j后判断是否在Set之中，如果是则入栈，接着判断下面的
                stack += [(i, j)]
                i = j + 1
        return False

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + [False] * len(s)
        wordDict = set(wordDict)
        for i in range(len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
        return dp[len(s)]


speedtest((Solution().wordBreak, Solution().wordBreak_slow), ("leetcode", ["leet", "code"]))
speedtest((Solution().wordBreak, Solution().wordBreak_slow), ("applepenapple", ["apple", "pen"]))
speedtest((Solution().wordBreak, Solution().wordBreak_slow), ("catsandog", ["cats", "dog", "sand", "and", "cat"]))
speedtest((Solution().wordBreak, Solution().wordBreak_slow), ("goalspecial", ["go", "goal", "goals", "special"]))
speedtest((Solution().wordBreak, Solution().wordBreak_slow), (
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
    ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]))
speedtest((Solution().wordBreak, Solution().wordBreak_slow), (
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    ["aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa", "ba"]))
