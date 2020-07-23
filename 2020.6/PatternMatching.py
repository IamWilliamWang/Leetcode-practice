from functools import lru_cache

from test_script import speedtest


class Solution:
    def patternMatching_offical(self, pattern: str, value: str) -> bool:
        count_a = sum(1 for ch in pattern if ch == 'a')
        count_b = len(pattern) - count_a
        if count_a < count_b:
            count_a, count_b = count_b, count_a
            pattern = ''.join('a' if ch == 'b' else 'b' for ch in pattern)

        if not value:
            return count_b == 0
        if not pattern:
            return False

        for len_a in range(len(value) // count_a + 1):
            rest = len(value) - count_a * len_a
            if (count_b == 0 and rest == 0) or (count_b != 0 and rest % count_b == 0):
                len_b = 0 if count_b == 0 else rest // count_b
                pos, correct = 0, True
                value_a, value_b = None, None
                for ch in pattern:
                    if ch == 'a':
                        sub = value[pos:pos + len_a]
                        if not value_a:
                            value_a = sub
                        elif value_a != sub:
                            correct = False
                            break
                        pos += len_a
                    else:
                        sub = value[pos:pos + len_b]
                        if not value_b:
                            value_b = sub
                        elif value_b != sub:
                            correct = False
                            break
                        pos += len_b
                if correct and value_a != value_b:
                    return True

        return False

    @lru_cache(maxsize=None)
    def findAll(self, s: str, value: str):  # 找出s在value中的所有位置
        result = []
        i = 0
        while True:
            i = s.find(value, i)
            if i == -1:
                break
            result += [i]
            i += len(value)
        return result

    @lru_cache(maxsize=None)
    def match(self, pattern: str, value: str, A: str, B: str) -> bool:  # 将A和B代替pattern中的ab是否就是value
        # i = 0
        # for a_or_b in pattern:
        #     i = value.find(A if a_or_b == 'a' else B, i)
        #     if i == -1:
        #         return False
        #     i += len(A) if a_or_b == 'a' else len(B)
        # return i == len(value)
        # 防止A或B中包含'a' or 'b'
        def isMatch(AStr, BStr) -> bool:
            return pattern.replace('a', '{$a}').replace('b', '{$b}').replace('{$a}', AStr).replace('{$b}',
                                                                                                   BStr) == value

        return isMatch(A, B) or isMatch(A, '') or isMatch('', A) or isMatch(B, '') or isMatch('', B)

    def patternMatching(self, pattern: str, value: str) -> bool:
        if not value:
            if not pattern:  # 空的pattern能match空的value（pattern不为空的话，AB都变成了''）
                return True
            if pattern.count('a') == len(pattern) or pattern.count('b') == len(pattern):  # pattern中a和b不能同时出现
                return True
            return False
        if not pattern:
            return not value  # 只有空的value才能match空的pattern
        if pattern[0] == 'b':
            pattern = pattern.replace('a', 'c').replace('b', 'a').replace('c', 'b')
        if pattern == '':  # ''
            return self.match(pattern, value, '', '')
        if pattern == 'a':  # 'a'
            return self.match(pattern, value, value, '')
        if pattern.startswith('aa'):  # 'aa开头'
            AStartIndexes = self.findAll(value, value[0])
            for secondAIndex in AStartIndexes[1:] + [len(value)]:  # 把从小到大的所有A都试一遍
                A = value[:secondAIndex]
                BStartIndex = pattern.find('b') * len(A)  # 前面一共几个a*len(A)
                if BStartIndex < 0 or BStartIndex >= len(value):  # 'aa开头全是a'，'aa'也包括
                    B = ''
                elif value.find(A, BStartIndex + 1) == -1:  # 'aa开头全是b'
                    BDupStr = value[BStartIndex:]
                    BDupCount = pattern.count('b')
                    B = BDupStr[:len(BDupStr) // BDupCount] if BDupCount else ''
                else:  # 'aa开头后面有a和b'
                    nextAStart = value.find(A, BStartIndex + 1)
                    B = value[BStartIndex:nextAStart] if nextAStart != -1 else ''
                if self.match(pattern, value, A, B):
                    return True
            return False
        elif pattern.startswith('ab'):  # 'ab开头'
            if pattern == 'ab':
                return True  # 'ab'
            AStartIndexes = self.findAll(value, value[0])
            if pattern.count('a') == 1:  # 'ab开头全是b'
                if self.match(pattern, value, value, ''):
                    return True
                if pattern.find('a', 2) != -1:
                    return False
                BDupCount = pattern.count('b')  # B有几次重复
                for BLen in range(len(value) // BDupCount + 1):  # 所有B可能的长度都试一遍
                    if BLen == 0:
                        if self.match(pattern, value, value, ''):
                            return True
                        continue
                    B = value[-BLen:]
                    found = True
                    for i in range(2, BDupCount + 1):
                        if value[-i * BLen:-i * BLen + BLen] != B:  # 没找到或者不是完全的dup
                            found = False
                            break
                    if found:
                        return True
                return False
            elif pattern.count('b') == 1:  # 'ab开头全是a'
                if self.match(pattern, value, '', value):
                    return True
                for ALen in range(1, len(value) + 1):  # 所有A可能的长度都试一遍
                    if value[:ALen] == value[-ALen:]:
                        A = value[:ALen]
                        for BLen in range(len(value) - len(A)):
                            # BLen = len(value) - len(A) * len(AStartIndexes)
                            B = value[ALen:ALen + BLen]
                            if self.match(pattern, value, A, B):
                                return True
                return False
            else:  # ab开头后面有a和b
                for ALen in range(len(value) // 2 + 1):
                    A = value[:ALen]
                    # BDupStr = value[len(A):AStartIndexes[1]]
                    # if pattern.count('a') != 1:
                    #     BDupCount = self.findAll(pattern, 'a')[1] - self.findAll(pattern, 'a')[0] - 1
                    # else:
                    #     BDupCount = len(pattern) - 1
                    # B = BDupStr[:len(BDupStr) // BDupCount] if BDupCount else ''
                    for BLen in range(len(value) - ALen):
                        B = value[ALen:ALen + BLen]
                        if self.match(pattern, value, A, B):
                            return True
                return False


speedtest([Solution().patternMatching_offical, Solution().patternMatching], ("abba", "dogcatcatdog"))
speedtest([Solution().patternMatching_offical, Solution().patternMatching], ("abba", "dogcatcatfish"))
speedtest([Solution().patternMatching_offical, Solution().patternMatching], ("aaaa", "dogcatcatdog"))
speedtest([Solution().patternMatching_offical, Solution().patternMatching], ("abba", "dogdogdogdog"))
speedtest([Solution().patternMatching_offical, Solution().patternMatching], ("", "dogcatcatdog"))
speedtest([Solution().patternMatching_offical, Solution().patternMatching], ("b", "dogcatcatdog"))
speedtest([Solution().patternMatching_offical, Solution().patternMatching], ("ab", ""))
speedtest([Solution().patternMatching_offical, Solution().patternMatching], ("a", ""))
speedtest([Solution().patternMatching_offical, Solution().patternMatching], ("ab", "dog"))
speedtest([Solution().patternMatching_offical, Solution().patternMatching], ("bbba", "xxxxxx"))
speedtest([Solution().patternMatching_offical, Solution().patternMatching], ("bbba", "xxxxxxy"))
speedtest([Solution().patternMatching_offical, Solution().patternMatching],
          ("aaaaab", "xahnxdxyaahnxdxyaahnxdxyaahnxdxyaauxuhuo"))
speedtest([Solution().patternMatching_offical, Solution().patternMatching], ("abb", "jwwwwjttwwwwjtt"))
speedtest([Solution().patternMatching_offical, Solution().patternMatching], ("baa", "rztyzzetkxyzbxytxebybxytxeby"))
speedtest([Solution().patternMatching_offical, Solution().patternMatching], ("abb", "dryqxzysggjljxdxag"))
speedtest([Solution().patternMatching_offical, Solution().patternMatching],
          ("babbbbbb", "omfrghpdfwwrfhgyphhwmwwhmmfghmmdowywfmfsmfmhjdpwrwmmpgooooo"))
