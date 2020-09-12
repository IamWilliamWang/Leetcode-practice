from test_script import speedtest, standard


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        num1 = [0] + list(map(int, num1))
        num2 = [0] * (len(num1) - len(num2)) + list(map(int, num2))
        i, j = len(num1) - 1, len(num2) - 1
        while i >= 0 and j >= 0:
            num1[i] += num2[j]
            if num1[i] >= 10:
                num1[i] -= 10
                num1[i - 1] += 1
            i -= 1
            j -= 1
        while len(num1) > 1 and num1[0] == 0:
            del num1[0]
        return ''.join(map(str, num1))


speedtest(standard(Solution().addStrings, '0'), ('0', '0'))
speedtest(standard(Solution().addStrings, '108'), ('9', '99'))
speedtest(standard(Solution().addStrings, '168900064'), ('71', '168899993'))
