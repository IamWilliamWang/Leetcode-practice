from typing import List
from itertools import permutations


class Solution:
    def permutation(self, s: str) -> List[str]:
        result = set()
        for tuple in permutations(s, len(s)):
            result.add(''.join(tuple))
        return list(result)


print(Solution().permutation('abc'))
