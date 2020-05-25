class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.strip().split()
        if '' in words:
            words.remove('')
        words.reverse()
        return ' '.join(words)


print(Solution().reverseWords('I am apple.'))
