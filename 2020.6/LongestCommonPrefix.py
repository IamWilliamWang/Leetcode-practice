from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        for tpl in zip(*strs):
            if not all([True if ch == tpl[0] else False for ch in tpl]):
                break
            prefix += tpl[0]
        return prefix
