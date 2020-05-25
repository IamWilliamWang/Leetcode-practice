import sys

def getReversePairCount(nums: list):
    result = 0
    for i in range(numsLength):
        for j in range(i + 1, numsLength):
            if nums[i] > nums[j]:
                result += 1
    return result


numsLength = 2 ** int(sys.stdin.readline().strip())
originalNums = list(map(int, sys.stdin.readline().strip().split()))
askTimes = int(sys.stdin.readline().strip())
asks = list(map(int, sys.stdin.readline().strip().split()))
tmpNums = originalNums.copy()
for askTime in range(askTimes):
    groupLen = 2 ** asks[askTime]
    for i in range(0, numsLength, groupLen):
        tmpGroup = tmpNums[i:i + groupLen]
        tmpGroup.reverse()
        tmpNums[i:i + groupLen] = tmpGroup
    print(getReversePairCount(tmpNums))
