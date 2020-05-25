class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substrings = []
        substring = []
        for ch in s:
            if ch in substring:
                substrings += [substring]
                try:
                    substring = substring[substring.index(ch) + 1:]
                except:
                    substring = []
            substring += [ch]
        substrings += [substring]
        return max([len(substr) for substr in substrings])


print(Solution().lengthOfLongestSubstring('abcabcbb'))
