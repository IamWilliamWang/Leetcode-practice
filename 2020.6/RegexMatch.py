import re
from collections import defaultdict
from functools import lru_cache


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def buildTransferDict():
            statusConvert = defaultdict(list)
            statusID = 0  # 当前所在的状态id（id=0代表start状态节点）
            statusIDNew = 0  # 转移后的新状态对应的id
            i = 0
            while i < len(p):
                if 'a' <= p[i] <= 'z' or p[i] == '.':
                    if i < len(p) - 1 and p[i + 1] == '*':  # 新节点带*号
                        statusIDNew += 1
                        statusConvert[statusID].append((p[i], statusIDNew))  # now->next条件：p[i]（保证可以{1}）
                        statusConvert[statusID].append((None, statusIDNew))  # now->next条件：epsilon（保证可以{0}）
                        statusConvert[statusIDNew].append((p[i], statusIDNew))  # next->next条件：p[i]（保证可以{2,}）
                        statusID = statusIDNew  # 状态转换
                        i += 1  # 跳过*号，加速循环
                    else:
                        statusIDNew += 1
                        statusConvert[statusID].append((p[i], statusIDNew))  # now->next条件：p[i]（保证可以{1}）
                        statusID = statusIDNew
                i += 1
            statusConvert[statusID].append((None, None))  # 最后一个状态指向id=None的状态（id=None代表end状态节点）
            return statusConvert

        @lru_cache(maxsize=None)
        def match(i: int, nowStatusID: int) -> bool:
            if i == len(s):
                if nowStatusID in statusConvert and statusConvert[nowStatusID][-1] == (None, None):
                    return True
                return False
            for convertCh, nextStatusId in statusConvert[nowStatusID]:
                if (convertCh == '.' or convertCh == s[i]) and match(i + 1, nextStatusId):
                    return True
                if convertCh is None and match(i, nextStatusId):
                    return True
            return False

        s += '.'  # 当p[-1]是'*'时可能会出现s完了p还有几个*导致返回False。分别添加一个.可以强迫跳过中间的多个*，找到最后的.
        p += '.'
        statusConvert = buildTransferDict()
        return match(0, 0)


cu = lambda s, p: re.findall('^' + p + '$', s) != []
while True:
    inputStr = input('>> ')
    print(Solution().isMatch(*inputStr.split()), end=' ')
    print(cu(*inputStr.split()))
