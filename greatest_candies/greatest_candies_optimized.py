from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        return [(candy + extraCandies >= max_candy) for candy in candies]


candies = [2, 3, 5, 1, 3]
extraCandies = 3

sol = Solution()
result = sol.kidsWithCandies(candies, extraCandies)
print(result)
