from typing import List


class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        favoriteCompanySets = [set(company) for company in favoriteCompanies]
        nonIndependentSetIndex = []
        for i in range(len(favoriteCompanies)):
            if i in nonIndependentSetIndex:
                continue
            for j in range(i + 1, len(favoriteCompanies)):
                inter = favoriteCompanySets[i].intersection(favoriteCompanies[j])
                if inter == favoriteCompanySets[j]:
                    nonIndependentSetIndex.append(j)
                elif inter == favoriteCompanySets[i]:
                    nonIndependentSetIndex.append(i)
        result = list(range(len(favoriteCompanies)))
        nonIndependentSetIndex = list(set(nonIndependentSetIndex))
        for removed in nonIndependentSetIndex:
            result.remove(removed)
        return result


print(Solution().peopleIndexes(
    favoriteCompanies=[["leetcode", "google", "facebook"], ["leetcode", "amazon"], ["facebook", "google"]]))
