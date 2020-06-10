class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        editTimes = 0
        while i < j:
            if s[i] != s[j]:
                if s[i] == s[j - 1]:
                    editTimes += 1
                    j -= 1
                elif s[i + 1] == s[j]:
                    editTimes += 1
                    i += 1
                elif j < len(s) - 1 and s[i] == s[j + 1]:
                    editTimes += 1
                    j += 1
                elif i > 0 and s[i - 1] == s[j]:
                    editTimes += 1
                    i -= 1
                else:
                    return False
            i += 1
            j -= 1
        return editTimes <= 1

    def validPalindrome2(self, s: str, depth=0) -> bool:
        if depth > 1:
            return False
        if len(s) == 1:
            return True
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return self.validPalindrome2(s[0:i] + s[i + 1:], depth + 1) or self.validPalindrome2(s[0:j] + s[j + 1:], depth + 1)
            i += 1
            j -= 1
        return True


print(Solution().validPalindrome2("yd"))
