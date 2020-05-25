class Solution:
    def subarraysWithKDistinct(self, A: list, K: int) -> int:
        subArrays = []
        for i in range(len(A) - K + 1):
            for j in range(i + K - 1, len(A)):
                if len(set(A[i:j + 1])) == K:
                    subArrays += [A[i:j + 1]]
        return len(subArrays)
