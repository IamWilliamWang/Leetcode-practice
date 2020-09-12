#
#
# @param str1 string字符串 原始的字符串
# @param str2 string字符串 转换的字符串
# @return string字符串
#
from collections import Counter
from itertools import zip_longest


class Solution:
    def find_diff_char(self, str1: str, str2: str):
        counters = [Counter(str1), Counter(str2)]
        for key1, key2 in zip_longest(counters[0].keys(), counters[1].keys()):
            if not key1 or not key2:
                return key1 or key2
            if key1 != key2:
                return key2
            if counters[0][key1] != counters[1][key2]:
                return key2


print(Solution().find_diff_char("abcd", "abcde"))
