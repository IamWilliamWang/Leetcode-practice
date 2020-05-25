class Solution:
    def getLongstrLoopLeastTimesToContainsShortstr(self, longStr: str, shortStr: str, timesMaxLimit=0):
        index = -1
        ans = 1
        for shortCh in shortStr:
            if 0 < timesMaxLimit <= ans:
                break
            foundIndex = (longStr * 2).find(shortCh, index + 1)
            if foundIndex == -1:
                return -1
            if foundIndex >= len(longStr):
                index = foundIndex - len(longStr)
                ans += 1
            else:
                index = foundIndex
        return ans

    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        s2 = s2 * n2
        M = 0
        while True:
            least = self.getLongstrLoopLeastTimesToContainsShortstr(s1, s2 * (M + 1), n1+1)
            if least == -1:
                return 0
            if least <= n1:
                M += 1
                continue
            break
        return M



def hcf(x:int,y:int)->int:
    hcf=1
    if x>y:
        small=y
    else:
        small=x
    for i in range(1,small+1):
        if x%i==0 and y%i==0:
            hcf=i
    return hcf
# print(Solution().getMaxRepetitions("niconiconi",
# 99981,
# "nico",
# 81))
h=hcf(99981,3)
print(h)
print(Solution().getMaxRepetitions("niconiconi",
99981//h,
"nico",
3//h))