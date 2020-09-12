#
#
# @param chars string字符串一维数组
# @return string字符串
#
from collections import Counter
from functools import reduce
from typing import List


class Solution:
    def commonChars(self, chars: List[str]):
        if not chars:
            return ''
        if len(chars) == 1:
            return chars[0]
        sameChars = set(chars[0])
        for i in range(1, len(chars)):
            sameChars.intersection_update(chars[i])
            sameChars.intersection_update(chars[i])
        counters = [Counter(s) for s in chars]
        outputCounter = {}
        for sameChar in sameChars:
            time = reduce(lambda x, y: min(x, y), (counter[sameChar] for counter in counters))
            outputCounter[sameChar] = time
        output = ''
        for ch in chars[0]:
            if ch in outputCounter:
                output += ch
                outputCounter[ch] -= 1
                if outputCounter[ch] == 0:
                    del outputCounter[ch]
        return output


print(Solution().commonChars(["bella", "label", "roller"]))
