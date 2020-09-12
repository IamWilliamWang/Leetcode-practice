from functools import lru_cache


@lru_cache(maxsize=None)
def longestPalindrome(s: str):
    """
    中心扩散法实现最大子回文的计算
    :param s:
    :return:
    """
    maxPalindrome = ''
    maxLen = 0
    for centerIndex in range(len(s)):  # 每一个ch都有可能是子回文的中心
        startIndex, endIndex = centerIndex, centerIndex  # 指向子回文的第一个和最后一个ch的指针
        length = 1  # 当前状态的子回文长度
        # 先向左找到第一个和当前ch不一样的位置。（因为同一个字符不管重复多少次都是回文）
        while startIndex > 0 and s[startIndex - 1] == s[centerIndex]:
            startIndex -= 1
            length += 1
        # 向右寻找
        while endIndex < len(s) - 1 and s[endIndex + 1] == s[centerIndex]:
            endIndex += 1
            length += 1
        # 扩展两侧的边界，如果不满足回文就中断
        while startIndex >= 0 and endIndex < len(s) and s[startIndex] == s[endIndex]:
            startIndex -= 1
            endIndex += 1
            length += 2
        # 保存当前求得的最大子回文
        if length > maxLen:
            maxLen = length
            maxPalindrome = s[startIndex + 1:endIndex]  # 在startIndex和endIndex里面包含的字符串才是回文
    return maxPalindrome


def splitOnce(s: str, spliter: str):
    idx = s.index(spliter)
    result = [s[:idx], s[idx + len(spliter):]]
    for i in range(1, -1, -1):
        if not result[i]:
            del result[i]
    return result


string = input().strip()
for _ in range(int(input().strip())):
    begin, end = list(map(int, input().strip().split()))
    begin -= 1
    nowStrs = [string[begin:end]]
    times = 0
    while nowStrs:
        times += 1
        nowStr = nowStrs.pop()
        palindrome = longestPalindrome(nowStr)
        for s in splitOnce(nowStr, palindrome):
            if len(s) == 1:
                times += 1
                continue
            nowStrs.append(s)
    print(times)
