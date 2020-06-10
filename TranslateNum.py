from test_script import speedtest_format as speedtest


class Solution:
    def translateNum(self, num: int) -> int:
        def dp(i: int):
            nonlocal count
            if i >= len(numStr):
                count += 1
                return
            dp(i + 1)
            if i < len(numStr) - 1 and ('0' <= numStr[i] <= '1' or (numStr[i] == '2' and '0' <= numStr[i + 1] <= '5')):
                if numStr[i] != '0':  # 两位数不可以以0打头
                    dp(i + 2)

        numStr = str(num)
        count = 0
        dp(0)
        return count


speedtest([Solution().translateNum, lambda x: 2], [12])
speedtest([Solution().translateNum, lambda x: 1], [26])
speedtest([Solution().translateNum, lambda x: 1], [506])
speedtest([Solution().translateNum, lambda x: 1], [5006])
speedtest([Solution().translateNum, lambda x: 2], [50106])
speedtest([Solution().translateNum, lambda x: 2], [18580])
speedtest([Solution().translateNum, lambda x: 4], [185810])
