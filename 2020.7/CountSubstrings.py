from test_script import shuffle


class Solution:
    def countSubstrings(self, s: str) -> int:
        resultList = []
        for centerI in range(len(s)):
            left, right = centerI, centerI
            resultList.append(s[centerI])
            while 0 < left <= right < len(s) - 1 and s[left - 1] == s[right + 1]:  # len为单数
                left -= 1
                right += 1
                resultList.append(s[left:right + 1])
            if centerI < len(s) - 1 and s[centerI] == s[centerI + 1]:  # len为双数
                left, right = centerI, centerI + 1
                resultList.append(s[left:right + 1])
                while 0 < left <= right < len(s) - 1 and s[left - 1] == s[right + 1]:
                    left -= 1
                    right += 1
                    resultList.append(s[left:right + 1])
        return len(resultList)
