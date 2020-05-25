from typing import List, Iterator
class Solution:
    def singleNumbers(self, nums: List[int]) -> Iterator[int]:
        # singleNumbers = set()
        # nonSingleNumbers = set()
        # for num in nums:
        #     if num not in nonSingleNumbers and num not in singleNumbers:
        #         singleNumbers.add(num)
        #         continue
        #     if num in nonSingleNumbers:
        #         continue
        #     if num in singleNumbers:
        #         singleNumbers.remove(num)
        #         nonSingleNumbers.add(num)
        # return list(singleNumbers)
        from collections import Counter
        # result = []
        for targetNum, _ in list(filter(lambda dictItem: dictItem[1] == 1, list(Counter(nums).items()))):
            yield targetNum  # result.append(targetNum)
        # for targetNum in [dictTuple[0] if dictTuple[1] == 1 else None for dictTuple in list(Counter(nums).items())]:
        #     result.append(targetNum) if targetNum is not None else None
        # return result


print(list(Solution().singleNumbers(
    [60, 247, 248, 22, 144, 57, 243, 79, 174, 146, 211, 46, 121, 78, 39, 148, 16, 110, 36, 153, 100, 116, 190, 225, 216,
     98, 151, 177, 67, 9, 29, 121, 192, 11, 189, 118, 124, 110, 30, 245, 119, 248, 129, 120, 145, 208, 28, 149, 208,
     169, 7, 27, 225, 231, 167, 213, 129, 68, 98, 243, 79, 38, 161, 181, 52, 8, 209, 28, 190, 121, 136, 111, 165, 45,
     25, 56, 6, 152, 15, 223, 37, 194, 152, 219, 14, 210, 190, 186, 220, 154, 120, 1, 20, 127, 250, 60, 234, 48, 82,
     144, 226, 98, 133, 117, 2, 204, 163, 111, 98, 112, 8, 44, 204, 190, 32, 233, 210, 37, 119, 19, 94, 75, 225, 42,
     101, 133, 67, 38, 70, 188, 235, 228, 226, 220, 218, 108, 88, 46, 61, 138, 113, 189, 7, 142, 175, 116, 195, 128,
     121, 58, 41, 147, 122, 176, 222, 157, 45, 30, 229, 199, 243, 122, 42, 45, 82, 87, 166, 70, 174, 139, 242, 233, 54,
     188, 229, 15, 8, 7, 145, 228, 104, 24, 219, 109, 26, 239, 23, 246, 249, 249, 209, 158, 245, 125, 229, 114, 175, 42,
     64, 114, 190, 198, 15, 191, 5, 59, 107, 133, 226, 209, 138, 170, 192, 236, 136, 166, 224, 236, 141, 221, 36, 158,
     74, 177, 175, 164, 174, 175, 43, 78, 149, 57, 98, 232, 146, 49, 25, 74, 61, 179, 54, 224, 141, 69, 83, 1, 55, 83,
     12, 45, 96, 194, 193, 112, 182, 108, 170, 14, 52, 48, 30, 38, 112, 167, 180, 145, 210, 187, 124, 172, 74, 64, 0, 2,
     40, 159, 213, 116, 38, 161, 118, 197, 193, 237, 87, 71, 166, 142, 167, 71, 72, 201, 142, 29, 28, 148, 224, 21, 208,
     44])))
