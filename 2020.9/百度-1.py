from collections import Counter

n = int(input().strip())
nums = list(map(int, input().strip().split()))
numsDict = Counter(nums)
if 0 not in numsDict:
    print('-1')
    exit(0)
if numsDict[5] < 9:
    print(0)
    exit(0)
print('5' * int(numsDict[5] // 9 * 9) + '0' * numsDict[0])
