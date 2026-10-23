from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        # Store the product of all elements to the left of each index
        prefix = 1
        for i in range(n): # the flow is from index 0 to end
            output[i] = prefix
            prefix *= nums[i]

        # Multiply by the product of all elements to the right
        suffix = 1
        for i in range(n - 1, -1, -1): # the flow is from the end to the beginning; the range(n-1, -1, -1) essentially means, the initial number is n-1, it will stop at -1, (just means 0 is the last index) and the step size is -1.
            output[i] *= suffix
            suffix *= nums[i]

        return output