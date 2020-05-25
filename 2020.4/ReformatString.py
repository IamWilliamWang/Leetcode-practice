class Solution:
    def reformat(self, s: str) -> str:
        numbers = list(filter(lambda x: '0' <= x <= '9', s))
        chars = list(filter(lambda x: 'a' <= x <= 'z', s))
        if abs(len(numbers) - len(chars)) > 1:
            return ''
        ans = ''
        if len(numbers) > len(chars):
            for i in range(len(chars)):
                ans += numbers[i] + chars[i]
            ans += numbers[-1]
        else:
            for i in range(len(numbers)):
                ans += chars[i] + numbers[i]
            if len(chars) > len(numbers):
                ans += chars[-1]
        return ans

print(Solution().reformat('ab123'))