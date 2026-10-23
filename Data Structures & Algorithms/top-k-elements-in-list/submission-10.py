from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) <= k:
            return nums

        K_dict = Counter(nums)
        
        K_list = list(dict(sorted(K_dict.items(),key=lambda item: item[1], reverse=True)))

        return K_list[0:k]
