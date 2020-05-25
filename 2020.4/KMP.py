class KMP:
    """
    模拟KMP算法。先用pattern生成next数组，然后调用时根据pattern和next数组进行字符串搜索
    """

    def __init__(self, pattern=''):
        self.next = []
        self.pattern = pattern
        self._compile(pattern)

    def _compile(self, pattern: str):
        """
        根据pattern生成next数组
        :param pattern: 模式字符串
        """
        self.next = [0, 1]
        next_i = 2  # next数组要插入的位置，即len(next)+1
        while next_i < len(pattern):  # next不能越界，保持和pattern一样长
            # 求最大子序列的长度
            子序列的长度 = [1]  # 默认为1
            可能的子序列长度 = 1
            # 逐个尝试所有可能的长度。并保证最长前缀与最长后缀不能为next_i前的全部字符串
            while 可能的子序列长度 < next_i:
                if pattern[:可能的子序列长度] == pattern[next_i - 可能的子序列长度:next_i]:
                    子序列的长度 += [可能的子序列长度 + 1]  # 如果前缀==后缀，则把这个长度+1放在list里
                可能的子序列长度 += 1
            self.next += [max(子序列的长度)]  # 最大子序列的长度
            next_i += 1  # 求next下一个位置的数字

    def search(self, string: str):
        """
        在string中搜索字符串self.pattern
        :param string: 待搜索的字符串
        :return: string中第一次出现pattern的索引号
        """
        if self.pattern == string:
            return 0
        string_compare_start = 0  # 每次比较时pattern左边与string对齐的位置
        string_i = string_compare_start  # 比较时指向string的指针
        pattern_j = 0  # 比较时指向pattern的指针
        while string_i < len(string):
            # 开始每回合的逐字比较，如果相同就跳到下一个字进行比较
            while string_i < len(string) and pattern_j < len(self.pattern) and string[string_i] == self.pattern[pattern_j]:
                string_i += 1
                pattern_j += 1
            if pattern_j == len(self.pattern):  # 如果pattern越界了，说明比较成功。pattern内的所有字符在string里都有
                return string_compare_start
            if string_i == len(string):  # 当string指针越界时跳出
                return -1
            string_compare_start += pattern_j - self.next[pattern_j] + 1  # 使用next数组，跳到下一次开始的位置
            string_i = string_compare_start  # 重置两个指针
            pattern_j = 0
        return -1

    @staticmethod
    def indexOf(original: str, searchedStr: str) -> int:
        """
        在original中搜索searchedStr。同内置函数str.find()
        :param original:
        :param searchedStr:
        :return:
        """
        return KMP(searchedStr).search(original)


print(KMP.indexOf('abcdabcdabcdefg', 'abcdabcde'))
