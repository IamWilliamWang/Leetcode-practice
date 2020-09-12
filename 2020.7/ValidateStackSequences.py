from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        myStack = []
        # push或者pop不为空
        while pushed and popped:
            if not myStack or myStack[-1] != popped[0]:  # 入栈的条件：myStack是空的或者不满足出栈的条件
                myStack.append(pushed.pop(0))
            else:  # 出栈的条件：栈不为空，而且满足出栈的条件
                myStack.pop()
                popped.pop(0)
        if not pushed:
            return myStack == popped[::-1]  # 满足出栈顺序
        if not popped:
            return True


print(Solution().validateStackSequences(pushed=[1, 2, 3, 4, 5], popped=[4, 5, 3, 2, 1]))
