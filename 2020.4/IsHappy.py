class Solution:
    def isHappy(self, n: int) -> bool:
        save = set()
        while True:
            num = 0
            for ch in str(n):
                num += int(ch) ** 2
            if num not in save:
                save.add(num)
                n = int(num)
            else:
                return False
            if num == 1:
                return True