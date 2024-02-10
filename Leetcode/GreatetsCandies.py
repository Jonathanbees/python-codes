from typing import List
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        print("Maxcandies = ",maxCandies)
        for i in range(len(candies)):
            total = candies[i] + extraCandies
            print("Total = ",total)
            if total >= maxCandies:
                candies[i] = True
            else:
                candies[i] = False
        return candies
# Test cases
print(Solution().kidsWithCandies([2,3,5,1,3], 3))  # [True, True, True, False, True]