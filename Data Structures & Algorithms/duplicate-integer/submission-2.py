class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set_length = len(set(nums))
        if len(nums) != nums_set_length:
            return True
        return False