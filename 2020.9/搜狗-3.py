#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 返回生成的新密码个数
# @param password string字符串 密码的数组字符串（长度小于50），例如 12345
# @return long长整型
#
class Solution:
    def getPasswordCount(self, password):
        result = 0

        def dp(l: list):
            nonlocal result
            if len(l) == len(password):
                if ''.join(map(str, l)) != password:
                    result += 1
                return
            tmp = int(password[len(l)]) + l[-1]
            dp(l + [tmp // 2])
            if tmp // 2 * 2 != tmp:
                dp(l + [tmp // 2 + 1])

        for first in range(10):
            dp([first])
        return result


print(Solution().getPasswordCount('123'))
