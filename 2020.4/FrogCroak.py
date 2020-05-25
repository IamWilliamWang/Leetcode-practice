class Frog:
    def __init__(self, ch=None):
        self._receiveChars = 'croak'
        self._croakedIndex = len(self._receiveChars) - 1


class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        frogs = []
        frogWillCroak = [[], [], [], [], []]

        def getFrogNeedReceiveCh(ch):
            if frogWillCroak['croak'.find(ch)] == []:
                return None
            return frogWillCroak['croak'.find(ch)][0]

        def getUnbusyFrog():
            return getFrogNeedReceiveCh('c')

        for ch in croakOfFrogs:
            if ch == 'c':
                unbusyFrog = getUnbusyFrog()
                if unbusyFrog is None:
                    newFrog = Frog('c')
                    frogs.append(newFrog)
                    frogWillCroak[('croak'.find(ch) + 1) % 5].append(newFrog)
                else:
                    frogWillCroak[('croak'.find(ch) + 1) % 5].append(frogWillCroak['croak'.find(ch)].pop(0))
                continue
            needThatFrog = getFrogNeedReceiveCh(ch)
            if needThatFrog is None:
                return -1
            else:
                frogWillCroak[('croak'.find(ch) + 1) % 5].append(frogWillCroak['croak'.find(ch)].pop(0))
        for i in range(1, len(frogWillCroak)):
            if frogWillCroak[i]:
                return -1
        return len(frogs)


print(Solution().minNumberOfFrogs('croakcroa'))
