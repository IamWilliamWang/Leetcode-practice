from collections import Counter, defaultdict
from test_script import timer, speedtest


class Solution:
    def minWindow_violent(self, s: str, t: str) -> str:
        def containsEach(start: int, end: int) -> bool:
            """
            s[start:end]包含t所有字符（就是题目上的意思）
            :param start:
            :param end:
            :return:
            """
            for targetChar in targetCounter:  # 遍历t中的每个字符
                if targetCounter[targetChar] > nowCounter.get(targetChar, 0):  # 如果发现s[start:end]某个字符的个数小于t中对应的字符个数
                    return False
            return True  # 一切顺利

        def adjustCounter(counter: defaultdict, windowEnd: int) -> None:
            """
            调整counter。只操作counterEndAt到windowEnd-1的字符（暴力解法的优化函数）
            :param counter:
            :param windowEnd:
            :return:
            """
            nonlocal counterEndAt  # counter指向的末尾index
            while counterEndAt < windowEnd:  # counter所包含的范围不够
                counter[s[counterEndAt]] += 1  # 把下一个字符放进去计数
                counterEndAt += 1  # counter现在指向的末尾index

        targetCounter = Counter(t)
        minResult = ''  # 所求的最小子串
        minLen = 2 ** 31 - 1  # 最小子串的长度
        # s[startAt:endAt]的长度一定大于len(t)
        for startAt in range(len(s) - len(t) + 1):
            nowCounter = defaultdict(int)  # 对于当前的start点，新建空的nowCounter
            counterEndAt = startAt  # counter指向的末尾index
            for endAt in range(startAt + len(t), len(s) + 1):  # endAt是可以等于len(s)，因为是exclusive
                adjustCounter(nowCounter, endAt)  # 代替nowCounter = Counter(s[startAt:endAt])，用于降低时间复杂度
                if containsEach(startAt, endAt):  # 如果s[startAt:endAt]包含t所有字符
                    if endAt - startAt < minLen:  # 判断是否要保存
                        minResult = s[startAt:endAt]
                        minLen = endAt - startAt
                    break  # 后面的没必要再比了
        return minResult

    def minWindow(self, s: str, t: str) -> str:
        def containsEach(start: int, end: int) -> bool:
            """
            s[start:end]包含t所有字符（就是题目上的意思）
            :param start:
            :param end:
            :return:
            """
            for targetChar in targetCounter:  # 遍历t中的每个字符
                if targetCounter[targetChar] > nowCounter.get(targetChar, 0):  # 如果发现s[start:end]某个字符的个数小于t中对应的字符个数
                    return False
            return True  # 一切顺利

        def adjustCounter(counter: defaultdict, windowStart: int, windowEnd: int) -> None:
            """
            调整counter。只操作counterEndAt到windowEnd-1的字符（暴力解法的优化函数）
            :param counter:
            :param windowEnd:
            :return:
            """
            nonlocal counterStartAt  # counter指向的首部index
            nonlocal counterEndAt  # counter指向的末尾index
            while counterStartAt < windowStart:
                counter[s[counterStartAt]] -= 1
                counterStartAt += 1
            while counterEndAt < windowEnd:  # counter所包含的范围不够
                counter[s[counterEndAt]] += 1  # 把下一个字符放进去计数
                counterEndAt += 1  # counter现在指向的末尾index

        targetCounter = Counter(t)
        minResult = ''  # 所求的最小子串
        minLen = 2 ** 31 - 1  # 最小子串的长度
        nowCounter = defaultdict(int)
        counterStartAt, counterEndAt = 0, 0  # counter的范围
        startAt, endAt = 0, len(t)  # 实际的范围
        # 滑动窗口一直滑动
        while True:
            while endAt <= len(s):  # 当窗口没从后面飞出去
                adjustCounter(nowCounter, startAt, endAt)  # 同步counter到当前位置
                if containsEach(startAt, endAt):  # 如果找到的话，停止滑动
                    if endAt - startAt < minLen:  # 记录最小结果
                        minResult = s[startAt:endAt]
                        minLen = endAt - startAt
                    break
                endAt += 1  # 窗口扩大
            # 窗口越界，说明查找完了
            if endAt > len(s):
                break
            while startAt <= len(s) - len(t):  # 当窗口的开端在合理的位置
                adjustCounter(nowCounter, startAt, endAt)
                if not containsEach(startAt, endAt):
                    break
                if endAt - startAt < minLen:
                    minResult = s[startAt:endAt]
                    minLen = endAt - startAt
                startAt += 1  # 窗口缩小
            # 窗口开始处越界，说明查找完了
            if startAt > len(s) - len(t):
                break
        return minResult

    def minWindow_noCounter(self, s: str, t: str) -> str:
        targetCounter = defaultdict(int)  # 储存t的Counter
        nowCounter = defaultdict(int)  # 储存当前substring的Counter（忽略t以外的字符）
        # 生成t的Counter，一经生成，不再改变
        for ch in t:
            targetCounter[ch] += 1
        # 初始化变量
        windowStart, windowEnd = 0, 0  # 窗口是[windowStart, windowEnd)
        valid = 0  # 当前窗口下nowCounter中有几种字符是与targetCounter中相等的
        minStr = ''
        minLen = 2 ** 31 - 1
        # 当窗口越界，结束循环
        while windowEnd < len(s):
            # 首先是挪动窗口的尾部
            if s[windowEnd] in t:  # 只需要管t中的那几个字符
                nowCounter[s[windowEnd]] += 1  # nowCounter记录（由于是右开区间所以要先修订nowCounter）
                if nowCounter[s[windowEnd]] == targetCounter[s[windowEnd]]:  # 检查这个字符有没有达到t中的出现频率
                    valid += 1  # 这个字符达到了，此时[windowStart, windowEnd+1)是满足题意的
            windowEnd += 1  # 由于是右开区间，所以要++
            # 然后是挪动窗口的首部
            while valid == len(targetCounter):  # 当前状态一直满足题目要求时，收缩首部
                # 记录答案
                if windowEnd - windowStart < minLen:
                    minLen = windowEnd - windowStart
                    minStr = s[windowStart:windowEnd]
                # 和上面的逻辑类似，不过因为左闭区间，所以后修订nowCounter
                if s[windowStart] in t:
                    if nowCounter[s[windowStart]] == targetCounter[s[windowStart]]:  # 如果删掉该字符，valid会受到影响
                        valid -= 1
                    nowCounter[s[windowStart]] -= 1
                windowStart += 1
        return minStr


speedtest((Solution().minWindow_violent, Solution().minWindow, Solution().minWindow_noCounter), (
    "sshcxyfgecymhhpmjrfjlmiwkaunetxwleajdfrjhrxrymdkdltoxbmjdhwhatfoafzfkqquhnlhcqrfdmwdnkmtrlaueiignjlazdwirhrtzladxygnjugcfiymqgsgpggqjcaclsxmdarcyzpjuxobimnytigkqodzsdedxbscblfclwlhuzkcmychiltyzwzscdxbhpekdlmojaxdbhhphmwpxsnwqposumwbdcognawycvcefltmxqcukrraihtdvrgztuhivggxbkdgwxvtpxozqhzzoueklklgfuocaxbehfkdehztepsxwtymocybojiveyzexbkfixkmelhjabiyuinkmloavywbyvhwysbipnwtzdebgocbwpniadjxbhyaegwdaznpokkppptwdvzckokksvkteivjqtoqubfjnqadhtzmoaoaobngwxabfxmwramlduurmxutqvfhvwhjxusttuwzrixikluqfqhtndmeaulvsugprakkuhjmriueuqubhdvwgjagfndxklmbmzlgixuzhpfbhzfqccnknnqtdvsphhqvgdboaypipvlwwsnzualipebuz",
    "tjiazd"))
# print(Solution().minWindow_violent(*args))
# print(Solution().minWindow(*args))
# print(Solution().minWindow_noCounter(*args))
