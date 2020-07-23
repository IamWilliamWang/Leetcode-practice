class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i, j = 0, len(s) - 1
        while i < j:
            while i < len(s) and not 'a' <= s[i] <= 'z' and not '0' <= s[i] <= '9':
                i += 1
            while j >= 0 and not 'a' <= s[j] <= 'z' and not '0' <= s[j] <= '9':
                j -= 1
            if i < j and s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


print(Solution().isPalindrome('.,'))
