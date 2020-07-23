from typing import List, Tuple
from collections import defaultdict
from functools import lru_cache

# positive cases: +100 -123 01 .5 -.6 5.60 13. +9e2 -1e3 5e+2 5e-1 1.6e1 3.e-2
# negetive cases: +-1 1-2 a1 .5+ . -. 5.60e 1.3. +9E2 -1e3.9 5a-1 1..6e1 1e- 6
'''
自动机：
0：开始状态
0->1 ~ + - eps
1：前面数字
1->1 ~ \d
1->2 ~ .
1->4 ~ e
1->7 ~ eps
2：小数点
2->3 ~ \d
2->4 ~ e
2->7 ~ eps
3：小数点后的数字
3->3 ~ \d
3->4 ~ e
3->7 ~ eps
4：e
4->5 ~ + - eps
5:前面的符号
5->6 ~ \d
6：e后面的数字
6->6 ~ \d
6->7 ~ eps
7：终点状态
'''
class Solution:
    def isNumber(self, s: str) -> bool:
        def build():
            """
            制作有穷限动机
            """
            NFA = {0: [(1, '+'), (1, '-'), (1, '')], 1: [(1, r'\d'), (2, '.'), (4, 'e'), (7, '')],
                   2: [(3, r'\d'), (4, 'e'), (7, '')], 3: [(3, r'\d'), (4, 'e'), (7, '')],
                   4: [(5, '+'), (5, '-'), (5, '')], 5: [(6, r'\d')], 6: [(6, r'\d'), (7, '')], 7: [(8, '#')]}
            return NFA, 8
        @lru_cache(maxsize=None)
        def match(strI: int, statusId, exist_number_before_e=False) -> bool:
            """
            可否到达终点状态
            :param strI: 当前未读取的指针
            :param statusId: 当前的状态
            :param exist_number_before_e: e前面是否有数字
            :return:
            """
            if statusId == endStatusId:  # 终止状态
                return strI == len(s) and exist_number_before_e  # 如果读完了所有字符，并且e前面部分包含数字
            if strI == len(s):  # 卡在中间状态出不去
                return False
            for toStatusId, transferCh in transfer[statusId]:
                if s[strI] == transferCh:  # 当字面上符合转移条件
                    if match(strI + 1, toStatusId, exist_number_before_e):  # 吃掉一个char，跳转到下个状态
                        return True
                if '0' <= s[strI] <= '9' and transferCh == r'\d':  # 当满足\d
                    if statusId < 4:  # 可以确定e的前面有数字
                        exist_number_before_e = True
                    if match(strI + 1, toStatusId, exist_number_before_e):
                        return True
                if transferCh == '':  # epsilon直接跳到下个状态
                    if match(strI, toStatusId, exist_number_before_e):
                        return True
            return False

        transfer, endStatusId = build()
        s = s.strip() + '#'  # 防止就差最后几个epsilon，结果strI到头了。所以需要强制跳过这几个epsilon找到终止符'#'
        # if s == '#':
        #     return False
        return match(0, 0)
        # if match(0, 0):
        #     # 就一个dot，会误判为True，特殊处理一下
        #     s = s[:-1]  # 把结束符删了
        #     if '.' in s:
        #         dotIndex = s.index('.')
        #         if (dotIndex - 1 >= 0 and '0' <= s[dotIndex - 1] <= '9') or (
        #                 dotIndex + 1 < len(s) and '0' <= s[dotIndex + 1] <= '9'):  # dot左边或者右边存在数字
        #             return True
        #         else:
        #             return False
        #     else:  # 别的不用管了
        #         return True
        # return False

# goods = '+100 -123 01 .5 -.6 5.60 13. +9e2 -1e3 5e+2 5e-1 1.6e1'.split(' ') + ["+100", "5e2", "-123", "3.1416", "0123"]
# bads = '+-1 1-2 a1 .5+ . -. 5.60e 1.3. +9E2 -1e3.9 5a-1 1..6e1 1e-'.split(' ') + ['1e- 6'] + ["12e", "1a3.14", "1.2.3",
#                                                                                               "+-5", "-1E-16",
#                                                                                               "12e+5.4"]
# for good in goods:
#     print(Solution().isNumber(good))
# print('-----------------------------')
# for bad in bads:
#     print(Solution().isNumber(bad))
# print(Solution().isNumber('6.e2'))