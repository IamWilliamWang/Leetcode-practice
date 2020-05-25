class Solution:
    def merge(self, intervals: list) -> list:
        intervals.sort()
        for i in range(1, len(intervals)):
            if intervals[i - 1][1] >= intervals[i][0]:
                intervals[i][0] = intervals[i - 1][0]
                if intervals[i - 1][1] > intervals[i][1]:
                    intervals[i][1] = intervals[i - 1][1]
                intervals[i - 1] = []
        while [] in intervals:
            intervals.remove([])
        return intervals


print(Solution().merge([[1,4],[0,2],[3,5]]))
