class Solution:
    def maxPower(self, s: str) -> int:
        if s == '':
            return 0
        s += '\n'  # 为了最后一个字符也能处理到
        counts = []
        count = 1
        for i in range(1, len(s)):
            if s[i - 1] == s[i]:  # 如果当前的等于上一个字符，增加count
                count += 1
            else:  # 否则，记录count并重置
                counts.append(count)
                count = 1
        return max(counts)


print(Solution().maxPower("l"))
