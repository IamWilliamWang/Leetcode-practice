class Solution:
    def numberOfSubarrays(self, nums: list, k: int) -> int:
        奇数的索引 = []
        def countArrays(first奇数IndexIn奇数List: int, last奇数IndexIn奇数List: int):
            left乘子, right乘子 = 奇数的索引[0] + 1, len(nums) - 奇数的索引[-1]
            if first奇数IndexIn奇数List > 0:
                left乘子 = 奇数的索引[first奇数IndexIn奇数List] - 奇数的索引[first奇数IndexIn奇数List - 1]
            if last奇数IndexIn奇数List < len(奇数的索引) - 1:
                right乘子 = 奇数的索引[last奇数IndexIn奇数List + 1] - 奇数的索引[last奇数IndexIn奇数List]
            return left乘子 * right乘子

        for numIndex in range(len(nums)):
            if nums[numIndex] % 2 == 1:
                奇数的索引.append(numIndex)
        result = 0
        for 第一个奇数的索引值 in range(len(奇数的索引) - k + 1):
            result += countArrays(第一个奇数的索引值, 第一个奇数的索引值 + k - 1)
        return result

    def numberOfSubarraysGroundTruth(self, nums: list, k: int) -> int:
        result = []
        for startAt in range(len(nums)):
            奇数的个数 = 0
            for endAt in range(startAt, len(nums)):
                if nums[endAt] % 2 == 1:
                    奇数的个数 += 1
                if 奇数的个数 == k:
                    result.append(nums[startAt:endAt + 1])
                elif 奇数的个数 > k:
                    break
        print(result)
        return len(result)


print(Solution().numberOfSubarrays([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], k=2))
