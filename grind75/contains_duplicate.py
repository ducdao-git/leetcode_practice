from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_set = set(nums)

        if len(num_set) < len(nums):
            return True
        else:
            return False
