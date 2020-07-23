from test_script import speedtest


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        def appendAndMerge(begin, end):
            nonlocal vaildSet
            chain = [tpl for tpl in vaildSet if tpl[1] == begin]
            if chain:
                tpl = chain[0]
                vaildSet.remove(tpl)
                vaildSet.add((tpl[0], end))
            else:
                superSet = [tpl for tpl in vaildSet if tpl[0] < begin and tpl[1] > end]
                if not superSet:
                    vaildSet.add((begin, end))

        stackIndex = []
        vaildSet = set()
        for i, ch in enumerate(s):
            if ch == '(':
                stackIndex.append(i)
            elif ch == ')':
                if not stackIndex:
                    continue
                begin = stackIndex.pop()
                end = i + 1
                appendAndMerge(begin, end)
        vaildLength = [end - begin for begin, end in vaildSet]
        return max(vaildLength + [0])


speedtest((Solution().longestValidParentheses, lambda x: 0), ["("])
speedtest((Solution().longestValidParentheses, lambda x: 2), ["()(()"])
speedtest((Solution().longestValidParentheses, lambda x: 6), ["()(())"])
speedtest((Solution().longestValidParentheses, lambda x: 8), ["((()))())"])
speedtest((Solution().longestValidParentheses, lambda x: 128), [
    "))()())))(()()()()((()()(())))()()()()))()())))(()()()()((()()(())))())))()(())))()())))(()()()()((()()(())))()()()()(())))((()()))()()()()(())))((())()))()())))(()()()()((()()(())))()(())))()(())))()())))(()()()()((()()(())))()()()()(())))((()()))()()()()(())))((())()))()())))(()()()()((()()(())))()()()()(())))(()()()()(())))(()(()()()()(())))(((())))(())))()(())))()())))(()()()()((()()(())))()()()()(())))((()()))()()()()(())))((())()))()())))(()()()()((()()(())))()()()()(())))(()((())))()(())))()())))(()()()()((()()(())))()()()()(())))((()()))()()()()(())))((())()))()())))(()()()()((()()(())))()()()()(())))(()((((())(()())(()()()()((()()()(()()())()())))(()())()())))(()()()()((()()(())))()()()()(())))(()()()((()()(())))()()()()(())))(()((())))()()()()(())))(((((()))()())()()())()("])
