from test_script import speedtest
from typing import Tuple
from collections import defaultdict
from functools import lru_cache


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def buildEdges() -> Tuple[dict, int]:
            statusId = 0
            edges = defaultdict(list)
            for patternCh in p:
                if patternCh != '*':
                    edges[statusId].append((patternCh, statusId + 1))
                    statusId += 1
                else:
                    edges[statusId].append(('', statusId + 1))
                    edges[statusId + 1].append(('?', statusId + 1))
                    statusId += 1
            endStatusId = statusId
            return edges, endStatusId

        @lru_cache(maxsize=None)
        def dfs(status: int, stringI: int) -> bool:
            if endStatusId == status:
                return stringI == len(s)
            if stringI == len(s):
                return edges[status][-1][0] == ('#', endStatusId)
            for edgeChar, toStatusId in edges[status]:
                if edgeChar == '?' or edgeChar == s[stringI]:  # 匹配一个字符
                    if dfs(toStatusId, stringI + 1):
                        return True
                elif edgeChar == '':  # epsilon
                    if dfs(toStatusId, stringI):
                        return True
            return False

        s += '#'
        p += '#'
        edges, endStatusId = buildEdges()
        return dfs(0, 0)


# speedtest([Solution().isMatch, lambda s, p: False], ['aa', 'a'])
# speedtest([Solution().isMatch, lambda s, p: True], ['aa', '*'])
# speedtest([Solution().isMatch, lambda s, p: False], ['cb', '?a'])
# speedtest([Solution().isMatch, lambda s, p: True], ['adceb', '*a*b'])
# speedtest([Solution().isMatch, lambda s, p: False], ['acdcb', 'a*c?b'])
# speedtest([Solution().isMatch, lambda s, p: True], ['a', 'a***'])
speedtest([Solution().isMatch, lambda s, p: False], ['', '?'])
speedtest([Solution().isMatch, lambda s, p: False], ['.', ''])
speedtest([Solution().isMatch, lambda s, p: True], ['', '*'])
while True:
    inputStr = input('>>> ').strip().split()
    print(Solution().isMatch(inputStr[0], inputStr[1]))