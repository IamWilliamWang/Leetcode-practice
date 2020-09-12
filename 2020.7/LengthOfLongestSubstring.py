class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        maxLen = 0
        strSet = set()
        while j < len(s):
            while j < len(s) and s[j] not in strSet:
                strSet.add(s[j])
                j += 1
            maxLen = max(maxLen, j - i)
            strSet.remove(s[i])
            i += 1
        return maxLen


print(Solution().lengthOfLongestSubstring("abcabcbb"))
