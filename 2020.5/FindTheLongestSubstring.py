from functools import lru_cache


class Solution:
    @lru_cache(maxsize=None)
    def match(self, startAt: int, lengthOfSubstring: int) -> bool:
        """
        判断该子串是否满足题目要求
        :param startAt: 子串从哪里开始
        :param lengthOfSubstring: 子串的长度
        :return:
        """
        endAt = startAt + lengthOfSubstring  # 子字符串结束地点
        for 某个元因字符 in self.aeiou在字符串的索引:
            appearedTimes = 0  # 每个元因出现的次数
            for 该元因出现的位置 in self.aeiou在字符串的索引[某个元因字符]:
                if startAt <= 该元因出现的位置 < endAt:
                    appearedTimes += 1
            if appearedTimes % 2:
                return False
        return True

    def findTheLongestSubstring(self, s: str) -> int:
        self.aeiou在字符串的索引 = {}
        # 统计所有元因的位置
        for i in range(len(s)):
            if s[i] in ['a', 'e', 'i', 'o', 'u']:
                self.aeiou在字符串的索引.setdefault(s[i], []).append(i)
        # 暴力查找
        for lengthOfSubstring in range(len(s), 0, -1):  # 从长到短暴力尝试
            for startAt in range(0, len(s) - lengthOfSubstring + 1):  # 子字符串的开始地点
                if self.match(startAt, lengthOfSubstring):  # 一旦找到了，就是符合题意的最大子串
                    return lengthOfSubstring
        return 0
