from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right = [0] * len(nums)
        left = [0] * len(nums)
        solution = nums.copy()
        for i in range(len(nums)-1):
            if i == 0:
                right[i] = 1
            else:
                right[i] = right[i] * nums[i+1]
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                left[i] = 1
            else:
                left[i] = left[i-1] * nums[i-1]
        for i in range(len(nums)):
            solution[i] = left[i] * right[i]
        return solution
# Test cases
print(Solution().productExceptSelf([5,2,3,4]))  # [24,60,40,30]
