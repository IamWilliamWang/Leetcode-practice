class Solution:
    def longestDupSubstring(self, S: str) -> str:
        dupSubString = ''
        # 从长到短每个长度都是一遍
        for substrLength in range(len(S) - 1, 0, -1):
            # 暴力比较，i和j指向长度为substrLength的子串
            for i in range(0, len(S) - substrLength + 1):  # i和j的条件消除了子串长度不为substrLength的情况
                for j in range(i + 1, len(S) - substrLength + 1):
                    if S[i:i + substrLength] == S[j:j + substrLength]:  # 如果子串相等，判断是否为更大的子串
                        subString = S[i:i + substrLength]
                        if len(dupSubString) < len(subString):
                            dupSubString = subString
        return dupSubString


print(Solution().longestDupSubstring('banana'))
