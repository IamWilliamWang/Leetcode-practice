from functools import lru_cache


@lru_cache(maxsize=None)
def expandOut(startIn: int, stopIn: int, changedCount: int) -> int:
    # 扩展两侧的边界
    while startIn >= 0 and stopIn < len(s):
        if s[startIn] == s[stopIn]:
            startIn -= 1
            stopIn += 1
        else:
            left, right = expandOut(startIn - 1, stopIn, changedCount + 1), expandOut(startIn, stopIn + 1, changedCount + 1)
            return min(left, right)  # 删掉左边一个或者右边一个
    else:
        if startIn < 0:
            return changedCount + len(s) - stopIn
        elif stopIn >= len(s):
            return changedCount + startIn+1


# s = input()
s = 'ldbsascbl'
changeCountMin = 2 ** 31 - 1
for centerIndex in range(len(s)):  # 每一个ch都有可能是子回文的中心
    startIndex, endIndex = centerIndex, centerIndex  # 指向子回文的第一个和最后一个ch的指针
    # 先向左找到第一个和当前ch不一样的位置。（因为同一个字符不管重复多少次都是回文）
    while startIndex > 0 and s[startIndex - 1] == s[centerIndex]:
        startIndex -= 1
    # 向右寻找
    while endIndex < len(s) - 1 and s[endIndex + 1] == s[centerIndex]:
        endIndex += 1
    ans = [changeCountMin]
    if endIndex != startIndex:
        ans += [expandOut(startIndex, endIndex - 1,0)]
    ans += [expandOut(startIndex, endIndex,0)]  # 把区域外的全删除光，加上这个区域需要删除几个
    changeCountMin = min(ans)
print(changeCountMin)
