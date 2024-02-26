from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)-1
        right = [0] * (length+1)
        left = [0] * (length+1)
        solution = nums.copy()
        print("Solución antes: ",solution)
        for i in range(length):
            if i == 0:
                left[i] = 1
            else:
                left[i] = left[i-1] * nums[i-1]
                print("Left: ", left)

        print("Left: ", left)
        for i in range(length, -1, -1):
            if i == length:
                right[i-1] = 1
            else:
                right[i-1] = right[i] * nums[i]
                print("Right: ", right)
        print("Right: ", right)
        for i in range(length):
            solution[i] = left[i] * right[i]
        print("Solución después: ",solution)
            
        return solution
        

            
    
# Test cases
print(Solution().productExceptSelf([5,2,3,4]))



