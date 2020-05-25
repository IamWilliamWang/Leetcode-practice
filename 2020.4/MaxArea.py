import random


class Solution:
    def maxArea(self, height: list) -> int:
        p, q = 0, len(height) - 1
        result = 0
        while p < q:
            result = max(result, min(height[p], height[q]) * (q - p))
            if height[p] < height[q]:
                p += 1
            else:
                q -= 1
        return result


# print([random.randint(0,10) for _ in range(random.randint(0, 100))])
print(Solution().maxArea([0, 1, 0, 4, 5]))