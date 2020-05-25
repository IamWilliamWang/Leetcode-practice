class Solution:
    def decodeString(self, s: str) -> str:
        numberStack = []
        charStack = []
        appendNumber = False
        for ch in s:
            if '0' <= ch <= '9':
                if not appendNumber:
                    numberStack.append(int(ch))
                else:
                    numberStack[-1] = numberStack[-1] * 10 + int(ch)
                appendNumber = True
            elif ch == '[' or 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
                appendNumber = False
                charStack.append(ch)
            elif ch == ']':
                appendNumber = False
                operatingChar = ''
                while True:
                    popedChar = charStack.pop()
                    if popedChar != '[':
                        operatingChar = popedChar + operatingChar
                    else:
                        time = numberStack.pop()
                        operatingChar = operatingChar * time
                        charStack += [ch for ch in operatingChar]
                        break
        result = ''
        for ch in charStack:
            result += ch
        return result


print(Solution().decodeString('HG[3|B[2|CA]]F'))
